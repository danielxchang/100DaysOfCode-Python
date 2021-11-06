from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip

DEFAULT_EMAIL = "daniel.changk@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    """
    generates random password, adds it to form, and copies to clipboard
    """
    random_password = password_generator.create_password()
    password_input.delete(0, END)
    password_input.insert(END, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    validates entry field values and saves login info to data.txt if valid and confirmed by user
    """
    # Retrieve entry fields values
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()

    if not website or not password:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email} "
                                                              f"\nPassword: {password} "
                                                              f"\nIs it ok to save?")
        if is_ok:
            # Write entry field values to data.txt file
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"\n{website} | {email} | {password}")

            # Clear website and password entry fields
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.eval('tk::PlaceWindow . center')

# Canvas with logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entry Widgets
website_input = Entry(width=36)
website_input.focus()
email_input = Entry(width=36)
email_input.insert(END, DEFAULT_EMAIL)
password_input = Entry(width=22)
website_input.grid(column=1, row=1, columnspan=2)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate)
add_button = Button(text="Add", width=37, command=save)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
