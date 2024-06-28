class QuizBrain:
    def __init__(self, q_list):
        self.question_num=0
        self.question_list=q_list
        self.score=0
    def next_question(self):
        cur_question=self.question_list[self.question_num]
        self.question_num+=1
        user_answer=input(f"{self.question_num}: {cur_question.text} (True/False)")
        self.check_answer(user_answer, cur_question.answer)
    def still_has_question(self):
        if self.question_num<len(self.question_list):
            return True
        else:
            return False
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("Thats Wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")