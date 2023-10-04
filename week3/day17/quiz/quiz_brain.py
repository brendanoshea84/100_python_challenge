
class QuizBrain:
    def __init__(self, q_list):
        self.quiz_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.quiz_number]
        self.quiz_number += 1
        user_guess = input(
            f"Q.{self.quiz_number}: {current_question.text} (True/False)")
        self.check_ans(user_guess, current_question.answer)

    def still_has_questions(self):
        return (self.quiz_number < len(self.question_list))

    def check_ans(self, user_guess, right_ans):
        if (user_guess.lower() == right_ans.lower()):
            print("correct")
            self.score += 1
        else:
            print("wrong")

        print(f"Your score is {self.score} / {self.quiz_number}")
        print(f"\n")
