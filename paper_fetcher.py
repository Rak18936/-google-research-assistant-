import os
import sys
import urllib.request
import feedparser
import json
import pandas as pd
import ssl

def print_header(title):
    print("\n" + "=" * 60)
    print(f" {title.center(58)} ")
    print("=" * 60)

def print_status(step, message):
    print(f"[{step.upper()}] {message}")

def fetch_arxiv_papers(query, max_results=5):
    """Queries the arXiv API for papers matching the search term."""
    print_status("Search", f"Querying arXiv for: '{query}'...")
    
    # Format query for URL
    formatted_query = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{formatted_query}&max_results={max_results}"
    
    try:
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)
        feed_data = response.read()
        
        feed = feedparser.parse(feed_data)
        papers = []
        
        for entry in feed.entries:
            authors = [author.name for author in entry.authors] if 'authors' in entry else []
            pdf_url = ""
            for link in entry.links:
                if link.rel == 'alternate':
                    pdf_url = link.href.replace('abs', 'pdf') + ".pdf"
                    
            papers.append({
                'title': entry.title.replace('\n', ' ').strip(),
                'id': entry.id.split('/abs/')[-1],
                'published': entry.published[:10],
                'authors': authors,
                'summary': entry.summary.replace('\n', ' ').strip(),
                'pdf_url': pdf_url
            })
            
        print_status("Success", f"Found and parsed {len(papers)} research papers.")
        return papers
        
    except Exception as e:
        print_status("Error", f"Failed to download from arXiv: {e}")
        return []

def save_papers(papers):
    """Saves the fetched paper metadata to the output directory."""
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    json_path = os.path.join(output_dir, 'fetched_papers.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=4, ensure_ascii=False)
        
    csv_path = os.path.join(output_dir, 'fetched_papers.csv')
    df = pd.DataFrame(papers)
    df.to_csv(csv_path, index=False, encoding='utf-8')
    
    print_status("Save", "Metadata successfully saved to:")
    print(f"  └─ JSON Index: {json_path}")
    print(f"  └─ CSV Spreadsheet: {csv_path}")

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print_header("GOOGLE RESEARCH ASSISTANT: PAPER FETCHER")
    
    query = input("\nEnter research topic (e.g., 'Large Language Models'): ").strip()
    if not query:
        query = "Large Language Models"
        
    papers = fetch_arxiv_papers(query)
    if papers:
        save_papers(papers)
        print_header("FETCHED PAPER SUMMARIES")
        for i, paper in enumerate(papers, 1):
            print(f"\n[{i}] {paper['title']}")
            print(f"    Authors: {', '.join(paper['authors'][:4])}")
            print(f"    Published: {paper['published']} | arXiv ID: {paper['id']}")
        print("\n" + "=" * 60 + "\n")

if __name__ == '__main__':
    main()
