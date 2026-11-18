"""Check basic consistency across the ShopFlow BA case-study files.

Run from the project folder:
    python validate_case_study.py

This checks document links and test-case references. It does not execute
the fictional checkout or perform actual UAT.
"""
import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_csv(filename):
    with (BASE_DIR / filename).open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    required_files = [
        "README.md",
        "business-requirements.md",
        "user-stories.md",
        "process-flow.md",
        "uat-test-cases.csv",
        "requirements-traceability.csv",
        "uat-execution-log.csv",
        "stakeholder-register.md",
    ]

    missing_files = [name for name in required_files if not (BASE_DIR / name).is_file()]
    if missing_files:
        print("MISSING FILES")
        for name in missing_files:
            print(f"- {name}")
        raise SystemExit(1)

    brd = (BASE_DIR / "business-requirements.md").read_text(encoding="utf-8")
    stories_text = (BASE_DIR / "user-stories.md").read_text(encoding="utf-8")
    requirement_ids = set(re.findall(r"BR-\d{2}", brd))
    story_ids = set(re.findall(r"### (US-\d{2})", stories_text))

    test_cases = read_csv("uat-test-cases.csv")
    traceability = read_csv("requirements-traceability.csv")
    execution_log = read_csv("uat-execution-log.csv")

    test_ids = [row["test_case_id"] for row in test_cases]
    duplicate_tests = sorted({test_id for test_id in test_ids if test_ids.count(test_id) > 1})
    invalid_story_refs = sorted({
        row["related_story"] for row in test_cases
        if row["related_story"] not in story_ids
    })

    mapped_requirements = {row["requirement_id"] for row in traceability}
    mapped_stories = {row["story_id"] for row in traceability}
    missing_requirements = sorted(requirement_ids - mapped_requirements)
    missing_stories = sorted(story_ids - mapped_stories)

    trace_test_refs = {
        test_id
        for row in traceability
        for test_id in row["test_case_ids"].split(";")
        if test_id
    }
    invalid_trace_tests = sorted(trace_test_refs - set(test_ids))
    log_ids = [row["test_case_id"] for row in execution_log]
    missing_log_tests = sorted(set(test_ids) - set(log_ids))

    checks = [
        ("Required project files", not missing_files),
        ("Unique UAT test case IDs", not duplicate_tests),
        ("UAT stories exist", not invalid_story_refs),
        ("All business requirements mapped", not missing_requirements),
        ("All user stories mapped", not missing_stories),
        ("Traceability test IDs exist", not invalid_trace_tests),
        ("Execution log covers all test cases", not missing_log_tests),
    ]

    print("SHOPFLOW CASE STUDY CHECK")
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")

    print(f"\nBusiness requirements: {len(requirement_ids)}")
    print(f"User stories: {len(story_ids)}")
    print(f"UAT test cases: {len(test_cases)}")
    print(f"Traceability rows: {len(traceability)}")
    print("\nNote: This checks document consistency only. UAT has not been executed.")

    if not all(passed for _, passed in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
