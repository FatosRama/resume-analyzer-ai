# resume-analyzer-ai# Resume Analyzer AI

A lightweight tool that compares a resume (PDF) against a job description (text) and reports skill matches, gaps, and an estimated ATS (Applicant Tracking System) compatibility score — powered by an LLM for semantic matching rather than simple keyword search.

## What it does

Given a resume and a job description, the script:

- Extracts and parses text from a PDF resume
- Extracts key requirements (skills, tools, qualifications) from the job description
- Semantically compares the two (not just exact string matching — e.g. it should recognize "Postgres" and "PostgreSQL" as the same skill)
- Outputs:
  - Matched skills
  - Missing / weak skills
  - An estimated ATS compatibility score
  - 2-3 concrete suggestions to improve the resume for this specific role

## Example usage

```bash
python main.py --resume data/sample_resumes/example_resume.pdf --job data/sample_job_descriptions/example_job.txt
```

Example output:

```
=== Resume Analysis Report ===
Matched Skills (8): Python, Git, REST APIs, PostgreSQL, Docker, Linux, React, CI/CD
Missing Skills (3): Kubernetes, GraphQL, Terraform
ATS Score: 74/100

Suggestions:
1. Add "Kubernetes" explicitly if you've used it in any project, even briefly.
2. Mention specific CI/CD tools by name (e.g. GitHub Actions) rather than just "CI/CD".
3. Consider a dedicated "Cloud & Infrastructure" section to surface AWS/Docker experience faster for ATS parsing.
```

## Tech stack

- Python 3.10+
- `pypdf` — PDF text extraction
- Google Gemini API (`gemini-2.5-flash`) — semantic comparison and suggestion generation
- `python-dotenv` — environment variable management

## Project structure

```
resume-analyzer-ai/
├── main.py                        # CLI entry point
├── resume_analyzer/
│   ├── __init__.py
│   ├── pdf_parser.py               # Extracts raw text from resume PDF and requirements from job description
│   ├
│   ├── matcher.py                  # Core LLM-based comparison logic
│   └── report.py                   # Formats and prints/saves the final report
├── tests/
│   └── test_matcher.py             # Unit tests for core logic
├── data/
│   ├── sample_resumes/             # Example resumes for testing
│   └── sample_job_descriptions/    # Example job descriptions for testing
├── .env.example                    # Template for API key config
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/<your-username>/resume-analyzer-ai.git
cd resume-analyzer-ai
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # then add your API key inside .env
```

## Running tests

```bash
python -m pytest tests/
```

