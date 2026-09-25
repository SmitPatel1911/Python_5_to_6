import csv

with open("ipl_match_scores.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Winner:", row["winner"])
