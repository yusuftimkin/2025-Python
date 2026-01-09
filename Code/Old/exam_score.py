scores = [156, 90, 10, 88, 188, 147, 30, 65]

total_score = 0
average_score = 0
highest_score = 0
lowest_score = 0

score_sum = sum(scores)

print(f"Sum of scores is {score_sum}.")

max_score = max(scores)

print(f"Max score is {max_score}.")

min_score = min(scores)

print(f"Min score is {min_score}.")

print(sorted(scores))

for i in scores:
    total_score += i

print(f"Total score is {total_score}.")

for i in scores:
    if highest_score < i:
        highest_score = i
        lowest_score = highest_score

for i in scores:
    if lowest_score > i:
        lowest_score = i
    
average_score = total_score / len(scores)

print(f"Average score is {round(average_score, 2)}.")

print(f"The highest score is {highest_score}.")

print(f"The lowest score is {lowest_score}.")