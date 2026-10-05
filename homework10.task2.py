scores = [45, 82, 67, 38, 90, 55, 72]


passed_scores = list(filter(lambda score: score >= 50, scores))
print(passed_scores)
raised_scores = list(map(lambda score: min(score + 5, 100) , passed_scores))
print(raised_scores)