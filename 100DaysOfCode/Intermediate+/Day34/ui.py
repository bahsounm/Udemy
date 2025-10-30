import tkinter
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)
        
        # Score Label
        self.score_label = tkinter.Label(text="Score: 0", font=("Arial", 15, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        # Question Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some Question Text", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # True and False Buttons
        image1 = tkinter.PhotoImage(file="images/true.png")
        self.correct_button = tkinter.Button(image=image1, bg=THEME_COLOR, bd=0, command=lambda: self.check_quiz_answer("True"))
        self.correct_button.grid(column=0,row=2, padx=20, pady=20)

        image2 = tkinter.PhotoImage(file="images/false.png")
        self.incorrect_button = tkinter.Button(image=image2, bg=THEME_COLOR, bd=0,command=lambda: self.check_quiz_answer("False"))
        self.incorrect_button.grid(column=1,row=2, padx=20, pady=20)

        self.get_next_question()
        
        # Closing the Window
        self.window.mainloop()

    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
        except:
            self.canvas.itemconfig(self.question_text, text="Completed the Quiz\n\nFinal Score {}/10".format(self.score), fill=THEME_COLOR)
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")
        else:
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)

    def check_quiz_answer(self, button_clicked):
        score, result = self.quiz.check_answer(button_clicked)
        self.score = score
        self.score_label.config(text="Score {}".format(score))
        if result:
            self.canvas.itemconfig(self.question_text, text="Correct ✅", fill="green")
        else:
            self.canvas.itemconfig(self.question_text, text="Incorrect ❌", fill="red")
        
        self.canvas.after(1000, self.get_next_question)

