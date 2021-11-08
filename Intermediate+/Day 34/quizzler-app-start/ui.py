from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

FONT = ("Arial", 20, "italic")


class QuizInterface:
    """
    Models the quiz UI
    """

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.question_canvas = Canvas(height=250, width=300)
        self.question_text = self.question_canvas.create_text(150, 125, text="Question goes here",
                                                              font=FONT, fill=THEME_COLOR, width=280)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        self.score_label.config(text=f"Score:  {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've answered {round((self.quiz.score / 10) * 100)}%"
                                                                     f" of the questions correct!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)