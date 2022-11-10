highest_scores = [78,65,58,59,65,66,69,64,90]

highest_score = 0
for score in highest_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)