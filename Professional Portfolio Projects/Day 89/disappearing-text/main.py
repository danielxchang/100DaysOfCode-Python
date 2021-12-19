import time
from tkinter import *

FONT_NAME = "Montserrat"


class Gui:
    def __init__(self):
        self.start_time = 0

        self.window = Tk()
        self.window.title('DISAPPEARING TYPIST')
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(padx=350, pady=100)

        self.text_box = Text(width=40, bd=0, font=(FONT_NAME, 22), highlightthickness=0, spacing1=1, wrap='word')
        self.text_box.grid(row=0, column=0)

        self.words_label = Label(font=(FONT_NAME, 20), fg="#cccccc")
        self.words_label.grid(row=1, column=0)
        self.initialize_round()

    def initialize_round(self):
        self.text_box.insert(END, "Start typing...")
        self.text_box.config(fg="#cccccc")
        self.words_label.config(text="0 words")
        self.text_box.focus()
        self.text_box.mark_set("insert", "%d.%d" % (0, 0))
        self.bind_start_typing()

    def check_timer(self):
        time_gap = time.time() - self.start_time
        if time_gap > 5:
            self.empty_textbox()
            self.text_box.unbind('<Any-KeyPress>')
            self.initialize_round()
        else:
            self.window.after(100, self.check_timer)

    def empty_textbox(self):
        self.text_box.delete('1.0', END)

    def start_typing(self, *args, **kwargs):
        self.empty_textbox()
        self.text_box.config(fg="black")
        self.start_timer()
        self.text_box.unbind('<Any-KeyPress>')
        self.text_box.bind('<Any-KeyPress>', self.update_word_count)
        self.window.after(100, self.check_timer)

    def update_word_count(self, *args, **kwargs):
        self.start_timer()
        text = self.text_box.get('1.0', END)
        n_words = len(text.split())
        self.words_label.config(text=f"{n_words} words")

    def start_timer(self, *args, **kwargs):
        self.start_time = time.time()

    def bind_start_typing(self):
        self.text_box.bind('<Any-KeyPress>', self.start_typing)


gui = Gui()
gui.window.mainloop()