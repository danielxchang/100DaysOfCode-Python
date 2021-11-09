from tkinter import *
import time
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CHECKMARK = "✓"
reps = 0
timer = None
account_sid = 'AC57a33e32f8abccc7ecee66067a26a29f'
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clock():
    window.after_cancel(timer)
    global reps
    reps = 0
    refresh_screen()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    change_background("start")
    change_heading(reps)
    seconds = get_seconds(reps)
    if reps < 7:
        if reps == 0:
            refresh_screen()
            change_heading(reps)
        reps += 1
    else:
        reps = 0
    countdown(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    if count == 0:
        global reps
        next_rep = format_time(get_seconds(reps))
        canvas.itemconfig(time_id, text=f"{next_rep}")
        change_background("stop")
        if (reps - 1) % 2 == 0:
            update_checkmarks((reps - 1) // 2 + 1)
        send_text_reminder()
        raise_above_all()
    else:
        remaining = format_time(count)
        canvas.itemconfig(time_id, text=f"{remaining}")
        global timer
        timer = window.after(1000, countdown, count - 1)


# ---------------------------- HELPER FUNCTIONS ------------------------------- #
def refresh_screen():
    change_background("start")
    timer_label.config(text="Timer")
    canvas.itemconfig(time_id, text="00:00")
    update_checkmarks(0)


def send_text_reminder():
    client = Client(account_sid, AUTH_TOKEN)
    client.messages.create(
        messaging_service_sid='MGdbdbce2db415f5108c04c169fd828d27',
        body="TIME IS UP",
        to=PHONE_NUMBER
    )


def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def get_seconds(step):
    if step == 7:
        minutes = LONG_BREAK_MIN
    elif step % 2 == 0:
        minutes = WORK_MIN
    else:
        minutes = SHORT_BREAK_MIN
    return minutes * 60


def update_checkmarks(num_checkmarks):
    checkmarks.config(text=f"{CHECKMARK * num_checkmarks}")


def change_heading(step):
    mode = "Break" if step % 2 == 1 else "Work"
    timer_label.config(text=mode)


def change_background(setting):
    color = YELLOW if setting == 'start' else PINK
    canvas.config(bg=color)
    window.config(bg=color)
    timer_label.config(bg=color)
    checkmarks.config(bg=color)


def format_time(seconds):
    return time.strftime("%M:%S", time.gmtime(seconds))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)
window.eval('tk::PlaceWindow . center')

timer_label = Label(text="Timer", font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 115, image=tomato_img)
time_id = canvas.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", command=start_timer, font=(FONT_NAME, 18), highlightthickness=0)
reset_btn = Button(text="Reset", command=reset_clock, font=(FONT_NAME, 18), highlightthickness=0)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
checkmarks.grid(column=1, row=3)

window.mainloop()
