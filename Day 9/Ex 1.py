student_scores={
    "Farzam": 71,
    "Yasir": 96,
    "Ammad": 86,
    "Ahmed": 88,
    "Suffian": 91,
}
student_grades={}
for key in student_scores:
    if student_scores[key]<70:
        student_grades[key]="Fail"
    elif student_scores[key]<80:
        student_grades[key]="Acceptable"
    elif student_scores[key]<90:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key]<100:
        student_grades[key]="Outstanding"
print(student_grades)