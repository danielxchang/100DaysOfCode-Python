from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import json

DEFAULT_EMAIL = "test.com"


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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not website or not password:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            write_to_json(new_data)
        else:
            # Updating and writing old data with new data
            data.update(new_data)
            write_to_json(data)
        finally:
            # Clear website and password entry fields
            website_input.delete(0, END)
            password_input.delete(0, END)


def write_to_json(new_data):
    """
    Writes new_data dictionary to json data.json file
    :param new_data: dictionary
    """
    with open("data.json", "w") as data_file:
        # Create new json file and write new_data to it
        json.dump(new_data, data_file, indent=4)


# ---------------------------- SEARCH WEBSITE LOGIN ------------------------------- #
def find_password():
    """
    finds password for website entered as input if exists in data.json file
    """
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if website in data:
            msg = f"{website}\n" \
                  f"Email: {data[website]['email']}\n" \
                  f"Password: {data[website]['password']}"
        else:
            msg = f"No details for {website} exists."

        messagebox.showinfo(title=website, message=msg)


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
website_input = Entry(width=22)
website_input.focus()
email_input = Entry(width=36)
email_input.insert(END, DEFAULT_EMAIL)
password_input = Entry(width=22)
website_input.grid(column=1, row=1)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
generate_button = Button(text="Generate Password", command=generate)
add_button = Button(text="Add", width=37, command=save)
search_button.grid(column=2, row=1)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
