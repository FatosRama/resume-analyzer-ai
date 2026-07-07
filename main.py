import argparse
from dotenv import load_dotenv
from resume_analyzer.pdf_parser import extract_text_from_pdf
from resume_analyzer.job_parser import load_job_description
from resume_analyzer.matcher import analyze_match
from resume_analyzer.report import print_report

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Analyze a resume against a job description.")
    parser.add_argument("--resume", required=True, help="Path to resume PDF")
    parser.add_argument("--job", required=True, help="Path to job description text file")
    args = parser.parse_args()

    resume_text = extract_text_from_pdf(args.resume)
    job_text = load_job_description(args.job)
    result = analyze_match(resume_text, job_text)
    print_report(result)

if __name__ == "__main__":
    main()