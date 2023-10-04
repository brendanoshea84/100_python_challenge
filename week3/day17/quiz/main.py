from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for a in question_data:
    q_text = a['text']
    q_ans = a['answer']
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print(f"Your final score is {quiz.score}")
