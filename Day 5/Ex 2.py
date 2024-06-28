student_scores=input("Input Student Scores: ")
for n in range(0, len(student_scores)):
    student_scores=int(student_scores[n])
print(student_scores)
highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(highest_score)
