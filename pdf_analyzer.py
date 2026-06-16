import os
import sys
import urllib.request
import ssl
import json
import re
from pypdf import PdfReader
from anthropic import Anthropic

json_path = 'output/fetched_papers.json'
pdf_dir = 'output/pdfs'
output_report_path = 'output/full_pdf_analysis.md'

def print_header(title):
    print("\n" + "=" * 60)
    print(f" {title.center(58)} ")
    print("=" * 60)

def print_status(step, message):
    print(f"[{step.upper()}] {message}")

def download_pdf(url, filepath):
    """Downloads a PDF file from a URL using an unverified SSL context."""
    print_status("Download", f"Fetching PDF: {url[:60]}...")
    try:
        context = ssl._create_unverified_context()
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        
        with opener.open(url) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print_status("Success", f"Saved to disk: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print_status("Error", f"Failed to download PDF: {e}")
        return False

def extract_text_from_pdf(filepath):
    """Extracts all text from a local PDF file using pypdf."""
    print_status("Extract", f"Loading text pages from: {os.path.basename(filepath)}...")
    try:
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        print_status("Success", f"Extracted {len(text):,} characters of text.")
        return text
    except Exception as e:
        print_status("Error", f"Text extraction failed: {e}")
        return ""

def locate_section_text(full_text, section_keywords):
    """Locates and extracts text following section header keywords (e.g., Methodology, Experiments)."""
    for keyword in section_keywords:
        pattern = rf"(?i)(?:\d+\.?\s+)?{keyword}\b"
        matches = list(re.finditer(pattern, full_text))
        if matches:
            start_idx = matches[0].start()
            section_block = full_text[start_idx:start_idx + 3500]
            return section_block
    mid = len(full_text) // 2
    return full_text[mid:mid + 3000]

def analyze_paper_offline(paper_title, full_text):
    """Performs offline regex-based parsing to extract methodology, experiments, and results."""
    print_status("Analysis", f"Parsing '{paper_title[:45]}...' locally...")
    
    methodology_keywords = ['methodology', 'method', 'architecture', 'proposed system', 'approach']
    experiment_keywords = ['experiment', 'evaluation', 'experimental setup', 'testing', 'dataset']
    result_keywords = ['result', 'discussion', 'performance', 'finding']
    
    method_block = locate_section_text(full_text, methodology_keywords)
    exp_block = locate_section_text(full_text, experiment_keywords)
    res_block = locate_section_text(full_text, result_keywords)
    
    report = f"## Deep Analysis: {paper_title}\n"
    report += "*Extracted offline using Python document intelligence filters.*\n\n"
    
    report += "### 💡 1. Core Methodology & Architecture\n"
    report += f"> {method_block[:1200].strip()}...\n\n"
    
    report += "### 🧪 2. Experimental Setup & Benchmarks\n"
    report += f"> {exp_block[:1200].strip()}...\n\n"
    
    report += "### 📊 3. Quantitative Results & Discussion\n"
    report += f"> {res_block[:1200].strip()}...\n\n"
    
    report += "---\n\n"
    return report

def analyze_paper_with_claude(client, paper_title, full_text):
    """Uses Claude API to extract and analyze methodology, experiments, and results from full text."""
    print_status("AI Analysis", f"Sending context of '{paper_title[:45]}...' to Claude...")
    
    methodology_keywords = ['methodology', 'method', 'architecture', 'proposed system', 'approach']
    experiment_keywords = ['experiment', 'evaluation', 'experimental setup', 'testing']
    result_keywords = ['result', 'discussion', 'performance', 'finding']
    
    extracted_context = (
        f"Paper Title: {paper_title}\n\n"
        f"[Methodology Section Snippet]:\n{locate_section_text(full_text, methodology_keywords)[:4000]}\n\n"
        f"[Experiments Section Snippet]:\n{locate_section_text(full_text, experiment_keywords)[:4000]}\n\n"
        f"[Results Section Snippet]:\n{locate_section_text(full_text, result_keywords)[:4000]}\n"
    )
    
    prompt = (
        "You are a Senior Academic Reviewer. Analyze the following extracted sections from a research paper.\n\n"
        f"EXTRACTED DATA:\n{extracted_context}\n"
        "TASK:\n"
        "Provide a detailed, critical analysis of the paper's:\n"
        "1. METHODOLOGY: Explain the core algorithm, system architecture, or math models used.\n"
        "2. EXPERIMENTS: Describe the datasets, control baselines, and evaluation metrics used.\n"
        "3. RESULTS: Detail the quantitative improvements, statistical significance, and limitations.\n\n"
        "Present your analysis in clean, structured markdown format."
    )
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text + "\n\n---\n\n"

def main():
    if not os.path.exists(json_path):
        print_status("Error", f"Metadata file '{json_path}' not found. Please run 'python paper_fetcher.py' first.")
        sys.exit(1)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        papers = json.load(f)
        
    os.makedirs(pdf_dir, exist_ok=True)
    
    print_header("GOOGLE RESEARCH ASSISTANT: PDF DEEP ANALYZER")
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    offline_mode = api_key is None
    client = None if offline_mode else Anthropic()
    
    # Available papers menu
    print("\nAvailable Papers:")
    for idx, paper in enumerate(papers, 1):
        print(f"  [{idx}] {paper['title']}")
        
    selection = input("\nEnter paper numbers to download & analyze (e.g., '1,3' or 'all'): ").strip().lower()
    
    selected_indices = []
    if selection == 'all':
        selected_indices = list(range(len(papers)))
    else:
        try:
            parts = [p.strip() for p in selection.split(',')]
            selected_indices = [int(p) - 1 for p in parts if p.isdigit() and 1 <= int(p) <= len(papers)]
        except Exception:
            selected_indices = []
            
    if not selected_indices:
        print_status("Warning", "No valid papers selected. Defaulting to first 2 papers.")
        selected_indices = [0, 1][:len(papers)]
        
    papers_to_analyze = [papers[i] for i in selected_indices]
    print_status("Start", f"Analyzing {len(papers_to_analyze)} selected papers...")
    
    full_report = "# Detailed Research Paper PDF Analysis\n"
    full_report += "*Generated by the AI-Powered Research Assistant (Document Intelligence Pipeline)*\n\n---\n\n"
    
    for i, paper in enumerate(papers_to_analyze, 1):
        print_header(f"ANALYZING PAPER: {paper['title'][:40]}...")
        pdf_path = os.path.join(pdf_dir, f"Paper_{paper['id']}.pdf")
        
        # Download
        if not download_pdf(paper['pdf_url'], pdf_path):
            continue
            
        # Extract text
        full_text = extract_text_from_pdf(pdf_path)
        if not full_text:
            continue
            
        # Analyze
        if offline_mode:
            paper_report = analyze_paper_offline(paper['title'], full_text)
        else:
            try:
                paper_report = analyze_paper_with_claude(client, paper['title'], full_text)
            except Exception as e:
                print_status("API Error", f"Claude failed: {e}. Falling back to offline extraction.")
                paper_report = analyze_paper_offline(paper['title'], full_text)
                
        full_report += paper_report
        
    # Save final report
    os.makedirs('output', exist_ok=True)
    with open(output_report_path, 'w', encoding='utf-8') as f:
        f.write(full_report)
        
    print_header("ANALYSIS PROCESS COMPLETED")
    print_status("Save", f"Detailed report saved to: {output_report_path}\n")

if __name__ == '__main__':
    main()
