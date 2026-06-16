# AI-Powered Research Assistant (Automated Literature Reviews)

A professional-grade document intelligence pipeline designed to automate scientific literature research. The system queries live academic APIs (arXiv), downloads research papers, extracts text from PDF layers, and compiles comprehensive literature review syntheses.

---

## 🎓 Google Student Researcher Alignment

* **Natural Language Understanding (NLU)**: Automated extraction of research objectives, methodology, and experimental results from unstructured PDFs.
* **Information Retrieval**: Live integration with academic databases (arXiv API) using custom queries.
* **Systems & Software Engineering**: Implementing robust data parsing pipelines, fault-tolerant network downloads, and an offline local compiler fallback.

---

## 📂 Project Architecture
```text
google_research_assistant/
│
├── paper_fetcher.py       # Queries arXiv API and downloads paper metadata
├── lit_review_agent.py    # Generates a synthesized literature review report
├── pdf_analyzer.py        # Downloads full PDFs, extracts text, and parses sections
├── requirements.txt       # Project dependencies
└── output/                # Auto-generated project deliverables
    ├── fetched_papers.json     # Parsed search results metadata
    ├── fetched_papers.csv      # Spreadsheet format of fetched papers
    ├── literature_review.md    # Synthesized literature review with comparative tables
    ├── full_pdf_analysis.md    # Deep methodology & results extraction report
    └── pdfs/                   # Directory containing downloaded full research PDFs
```

---

## 🚀 Setup & Execution Guide

### 1. Install Dependencies
Open your PowerShell/Terminal in this directory and run:
```bash
pip install -r requirements.txt
```

### 2. Search and Fetch Papers
Run the fetcher script to retrieve metadata:
```bash
python paper_fetcher.py
```
* **Input**: Enter any research topic (e.g., *"Prompt Caching"* or *"Anomaly Detection"*).
* **Output**: Top 5 papers will be fetched and saved in the `output/` folder.

### 3. Set your Claude API Key (Optional)
If you have an active key, load it into your environment:
* **PowerShell**: `$env:ANTHROPIC_API_KEY="your_actual_key_here"`
* **Command Prompt**: `set ANTHROPIC_API_KEY=your_actual_key_here`

*(If no key is configured or if the key is out of credits, the pipeline automatically switches to **Offline Mode** to run all SQL and compilation steps locally for free!)*

### 4. Compile the Literature Review
Run the agent script to build the synthesis report:
```bash
python lit_review_agent.py
```
* **Output**: Generates **`output/literature_review.md`** featuring:
  * Executive Summaries.
  * Side-by-side **Comparative Tables**.
  * Formal **IEEE** & **APA** bibliography references.

### 5. Download and Deep-Analyze PDFs
Run the analyzer script to pull full papers:
```bash
python pdf_analyzer.py
```
* **Interaction**: Choose specific paper numbers (e.g., `1,3`) or type `all` to analyze the entire list.
* **Output**: Downloads PDFs to `output/pdfs/` and compiles a detailed analysis of their **Methodology**, **Experiments**, and **Results** inside **`output/full_pdf_analysis.md`**.
