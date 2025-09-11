import data
import question_model as q
class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.questions_list = self.get_question_bank()
        self.score = 0

    def get_question_bank(self):
        question_bank = []

        for d in data.question_data:
            new_q = q.Question(d["text"], d["answer"])
            question_bank.append(new_q)
        return question_bank

    def next_question(self):
        current_q = self.questions_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"{self.question_number}: {current_q.text} (True/False): ")
        self.report(user_ans, current_q.answer)
    
    def report(self, user_a, actual_a):
        if user_a == actual_a:
            self.score += 1
            print(f"Your got it right!\nThe correct answer was {actual_a}\nYour current score is {self.score}/{self.question_number}\n\n")
        else:
            print(f"Your got it wrong!\nThe correct answer was {actual_a}\nYour current score is {self.score}/{self.question_number}\n\n")
    
    def play_quiz(self):
        while self.question_number < len(self.questions_list):
            self.next_question()
        print(f"You've completed the quiz\nYour final score was: {self.score}/{self.question_number}")
        