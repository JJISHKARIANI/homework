scores = []
scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)
scores.remove(45)
print(max(scores), "is a maximum score")
print(min(scores), "is a minimum score")
print(sum(scores) // len(scores), "is a average score")
print(sorted(scores))
passed_score = [i for i in scores if i >= 60]
print(f"passed scores:{passed_score}")