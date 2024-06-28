from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
n_quiz=QuizBrain(question_bank)
while n_quiz.still_has_question():
    n_quiz.next_question()
print("You've completed the Quiz.")
print(f"Your final score is:{n_quiz.score}/{len(question_bank)}")