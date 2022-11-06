from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    text_question = ques["text"]
    answer_question = ques["answer"]
    new_question = Question(text_question, answer_question)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
next = quiz.next_question()
while next:
    next = quiz.next_question()





