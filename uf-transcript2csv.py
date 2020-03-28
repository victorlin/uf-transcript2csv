import argparse
import json
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("i", metavar="records.json", help="Input JSON file")
parser.add_argument("o", metavar="records.csv", help="Output CSV file")
args = parser.parse_args()

grade_point_map = {
    "A": 4.0,
    "A-": 3 + 2.0 / 3,
    "B+": 3 + 1.0 / 3,
    "B": 3.0,
    "B-": 2 + 2.0 / 3,
    "C+": 2 + 1.0 / 3,
    "C": 2.0,
    "C-": 1 + 2.0 / 3,
    "D+": 1 + 1.0 / 3,
    "D": 1.0,
    "D-": 2.0 / 3,
    "S": 0,
    "P": 0,
}

with open(args.i) as f:
    records = json.load(f)

courses = [
    {
        **{
            "term": term["termDescription"],
            "source": source["sourceDescription"],
            "gradePointsEarned": float(course["hoursEarned"])
            * grade_point_map[course["grade"]],
        },
        **course,
    }
    for term in records["undergraduate"]["terms"]
    for source in term["creditSources"]
    for session in source["sessions"]
    for course in session["courses"]
]

pd.DataFrame.from_records(courses).to_csv(args.o, index=None)

print("Done.")
