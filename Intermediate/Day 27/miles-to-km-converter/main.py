from tkinter import *

FONT = ("Courier", 14)
COLOR = "beige"


def convert():
    try:
        miles = float(miles_input.get())
    except ValueError:
        miles = 0
    km = round(miles * 1.609, 2)
    conversion.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=10, pady=20, background=COLOR)
window.eval('tk::PlaceWindow . center')

# Create entry widget
miles_input = Entry(width=10, font=FONT)
miles_input.insert(END, 0)
miles_input.focus()
miles_input.grid(column=1, row=0)


# Create label widgets
miles_label = Label(text="Miles", font=FONT, background=COLOR)
km_label = Label(text="Km", font=FONT, background=COLOR)
equal_label = Label(text="is equal to", font=FONT, background=COLOR)
conversion = Label(text=0, font=FONT, background=COLOR)
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
conversion.grid(column=1, row=1)
km_label.grid(column=2, row=1)

# Create calculate button
button = Button(text="Calculate", command=convert, font=FONT)
button.grid(column=1, row=2)

window.mainloop()
