from google import genai
import json
import os
from dotenv import load_dotenv

load_dotenv()


def _get_client() -> genai.Client:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Add it to your environment or .env file.")
    return genai.Client(api_key=api_key)

def analyze_match(resume_text: str, job_text: str) -> dict:
    prompt = f"""You are a resume screening assistant. Compare the resume against the job description.

Resume:
{resume_text}

Job Description:
{job_text}

Return ONLY valid JSON, no other text, in this exact format:
{{
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "ats_score": 0-100,
  "suggestions": ["suggestion1", "suggestion2", "suggestion3"]
}}"""

    client = _get_client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    raw = response.text.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)