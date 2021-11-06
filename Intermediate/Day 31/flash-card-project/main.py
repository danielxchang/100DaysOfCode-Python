from tkinter import *
from tkinter import messagebox
import pandas
import random
from os import remove

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
ORIGINAL_CSV = "data/french_words.csv"
TO_LEARN_CSV = "data/words_to_learn.csv"
FRONT_TITLE = "French"
BACK_TITLE = "English"
current_card = None
flip_timer = None

try:
    words_to_learn = pandas.read_csv(TO_LEARN_CSV)
except FileNotFoundError:
    words_to_learn = pandas.read_csv(ORIGINAL_CSV)
finally:
    to_learn = words_to_learn.to_dict(orient='records')


def know_card():
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        messagebox.showinfo(message="CONGRATULATIONS! YOU'VE LEARNED EVERYTHING!")
        remove(TO_LEARN_CSV)
        idk_button.config(state="disabled")
        known_button.config(state="disabled")
    else:
        to_learn_df = pandas.DataFrame(to_learn)
        to_learn_df.to_csv(TO_LEARN_CSV, index=False)
        next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text=FRONT_TITLE, fill="black")
    canvas.itemconfig(word, text=current_card[FRONT_TITLE], fill="black")
    canvas.itemconfig(card_bg, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text=BACK_TITLE, fill="white")
    canvas.itemconfig(word, text=current_card[BACK_TITLE], fill="white")
    canvas.itemconfig(card_bg, image=back_image)


# ----------------------------------UI Window-----------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
idk_image = PhotoImage(file="images/wrong.png")
idk_button = Button(image=idk_image, highlightthickness=0, command=next_card)
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=know_card)
idk_button.grid(row=1, column=0)
known_button.grid(row=1, column=1)

flip_timer = window.after(3000, func=flip_card)
next_card()
window.mainloop()
