import requests
import time
from tkinter import *

BACON_IPSUM_ENDPOINT = 'https://baconipsum.com/api/?type=all-meat&sentences=2'
FONT_NAME = "Courier"
BG_COLOR = '#77E4D4'


def reformat_text(text):
    return " ".join(text.split())


def generate_random_text():
    response = requests.get(url=BACON_IPSUM_ENDPOINT)
    random_text = response.json()[0]
    return reformat_text(random_text)


def grade_typing_test(sample, answer):
    score = 0
    answer_words = answer.split()
    sample_words = sample.split()

    for i in range(len(sample_words)):
        try:
            if sample_words[i] == answer_words[i]:
                score += 1
        except IndexError:
            break

    accuracy = round((score / len(sample_words)) * 100)
    return score, accuracy


def start_timer(*args, **kwargs):
    global start_time
    start_time = time.time()
    print(start_time)


def end_timer(*args, **kwargs):
    global end_time
    end_time = time.time()
    print(end_time - start_time)


class Gui:
    def __init__(self):
        self.sample_text = ""
        self.start_time = 0
        self.end_time = 0
        self.n_words = 0

        self.window = Tk()
        self.window.title('TYPING SPEED TEST')
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(bg=BG_COLOR, padx=50, pady=20)

        self.info_frame = Frame(self.window, bg=BG_COLOR)
        self.words_label = Label(self.info_frame, text="",  font=(FONT_NAME, 20), bg=BG_COLOR, justify="right")
        self.words_label.grid(row=2, column=0, sticky='E')
        self.high_score_label = Label(self.info_frame, text="",  font=(FONT_NAME, 20), bg=BG_COLOR, justify="right")
        self.high_score_label.grid(row=0, column=0, sticky='E')
        self.accuracy_label = Label(self.info_frame, text="",  font=(FONT_NAME, 20), bg=BG_COLOR, justify="right")
        self.accuracy_label.grid(row=1, column=0, sticky='E')
        self.info_frame.grid(row=0, column=0, pady=(0, 20), sticky='E')

        self.text_frame = Frame(self.window, bg=BG_COLOR)
        self.sample_label = Label(
            self.text_frame,
            text="",
            bg='#FBF46D',
            font=(FONT_NAME, 18),
            wraplength=1000,
            justify='left',
            relief='sunken',
            bd=5,
            padx=30,
            pady=30
        )
        self.sample_label.grid(row=0, column=0, sticky="NESW")

        self.text_box = Text(self.text_frame, width=100, font=(FONT_NAME, 18), height=5)
        self.text_box.grid(row=1, column=0, pady=30, sticky="NESW")
        self.text_frame.grid(row=1, column=0)

        reset_btn = Button(self.window, text="Reset", command=self.initialize_test, font=(FONT_NAME, 18),
                               highlightthickness=0, relief='raised')
        reset_btn.grid(column=0, row=2, sticky='W')

        self.initialize_test()

    def initialize_test(self):
        self.text_box.config(state='normal')
        self.text_box.delete('1.0', END)
        self.sample_text = generate_random_text()
        self.n_words = len(self.sample_text.split())
        self.words_label.config(text=f"NUMBER OF WORDS: {self.n_words}")
        self.high_score_label.config(text=f"WPM: TBD")
        self.accuracy_label.config(text=f"ACCURACY: TBD")
        self.sample_label.config(text=self.sample_text)
        self.text_box.focus()
        self.bind_start_timer()
        self.bind_end_timer()

    def start_timer(self, *args, **kwargs):
        self.start_time = time.time()
        self.text_box.unbind('<Any-KeyPress>')

    def end_timer(self, *args, **kwargs):
        self.end_time = time.time()
        self.text_box.config(state='disabled')
        self.text_box.unbind('<Return>')
        self.calculate_wpm()

    def bind_start_timer(self):
        self.text_box.bind('<Any-KeyPress>', self.start_timer)

    def bind_end_timer(self):
        self.text_box.bind('<Return>', self.end_timer)

    def calculate_wpm(self):
        answer_text = self.text_box.get('1.0', END)
        n_words, accuracy = grade_typing_test(self.sample_text, answer_text)
        duration = self.end_time - self.start_time
        wpm = round(n_words / duration * 60)
        self.high_score_label.config(text=f"WPM: {wpm}")
        self.accuracy_label.config(text=f"ACCURACY: {accuracy}%")


gui = Gui()
gui.window.mainloop()