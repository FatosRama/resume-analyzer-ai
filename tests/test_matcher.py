from pathlib import Path

from resume_analyzer.pdf_parser import extract_text_from_pdf
from resume_analyzer.pdf_parser import load_job_description


DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def test_pdf_extraction_returns_string():
    text = extract_text_from_pdf(str(DATA_DIR / "example_resume.pdf"))
    assert isinstance(text, str)
    assert len(text) > 0

def test_job_description_loads():
    text = load_job_description(str(DATA_DIR / "example_job.txt"))
    assert isinstance(text, str)
    assert len(text) > 0