def print_report(result: dict):
    print("=== Resume Analysis Report ===")
    print(f"Matched Skills ({len(result['matched_skills'])}): {', '.join(result['matched_skills'])}")
    print(f"Missing Skills ({len(result['missing_skills'])}): {', '.join(result['missing_skills'])}")
    print(f"ATS Score: {result['ats_score']}/100\n")
    print("Suggestions:")
    for i, s in enumerate(result['suggestions'], 1):
        print(f"{i}. {s}")