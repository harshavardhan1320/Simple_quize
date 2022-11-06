class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)? :")
        correct = True
        while correct:
            if current_question.answer == ans:
                print(f"your score is {self.question_number}")
                return True
            else:
                print(f"your final score is {self.question_number - 1}")
                print("you have loose the game :( ")
                return False

