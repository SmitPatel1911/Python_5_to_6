ipl_scores = [101, 98, 120, 77, 88]

# Lambda function to keep only even numbers
even = list(filter(lambda x: x % 2 == 0, ipl_scores))

print("Even Scores : ",even)

