from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
BG_COLOR = '#856ff8'


def retrieve_image(file_path):
    global filename
    opened_image = Image.open(file_path)
    filename = opened_image.filename.split('/')[-1]
    return resize_image(opened_image)


def display_image(image, file_path):
    tk_image = ImageTk.PhotoImage(image)
    image_label.config(image=tk_image)
    image_label.image = tk_image
    file_label.config(text=f"Uploaded: {file_path.split('/')[-1]}")


def select_file():
    global current_img
    try:
        file_path = fd.askopenfilename()
        image = retrieve_image(file_path)
        display_image(image, file_path)
        current_img = image
        download_btn.config(state='disabled')
    except AttributeError:
        pass


def resize_image(image):
    width, height = image.size
    factor = 500 / width
    new_size = (500, int(round(height * factor)))
    return image.resize(new_size, Image.ANTIALIAS)


def add_watermark():
    global watermark_image
    watermark_text = text_box.get('1.0', END)
    watermark_image = current_img.copy()
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype(FONT_NAME, 50)
    draw.text((0, 0), watermark_text,
              (255, 255, 255), font=font)
    display_image(watermark_image, "watermarked")
    download_btn.config(state='active')
    file_label.config(text="Success! Ready to Download!")


def download():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, f'wm-{filename}')
    watermark_image.save(file_path)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('WATERMARK IT')
window.eval('tk::PlaceWindow . center')
window.config(padx=100, pady=100, bg=BG_COLOR)

top_frame = Frame(window, bg=BG_COLOR, padx=20)
top_frame.grid(column=1, row=0, sticky='NW')

file_btn = Button(top_frame, text="Select a File", command=select_file, font=(FONT_NAME, 18),
                  highlightthickness=0, width=25)
file_btn.grid(column=0, row=0, sticky='W')
file_label = Label(top_frame, text="", bg=BG_COLOR, font=(FONT_NAME, 18), pady=10, wraplength=275, justify='left')
file_label.grid(column=0, row=1, sticky='W')
download_btn = Button(top_frame, state='disabled', text="Download Photo", command=download,
                      font=(FONT_NAME, 18), highlightthickness=0, width=25)
download_btn.grid(column=0, row=2, sticky='W')

bottom_frame = Frame(window, bg=BG_COLOR, padx=20)
bottom_frame.grid(column=1, row=1, sticky='WS')

text_label = Label(bottom_frame, text="Enter Watermark Logo/Text:", bg=BG_COLOR, font=(FONT_NAME, 18))
text_label.grid(column=0, row=1, sticky='W')
text_box = Text(bottom_frame, highlightthickness=0, width=30, height=5)
text_box.grid(column=0, row=2, sticky='W', pady=20)
watermark_btn = Button(bottom_frame, text="Add Watermark", command=add_watermark, font=(FONT_NAME, 18),
                       highlightthickness=0)
watermark_btn.grid(column=0, row=4, sticky='W')

image_label = Label(window)
image_label.grid(column=0, row=0, rowspan=2)
filename = 'upload.png'
current_img = retrieve_image(filename)
display_image(current_img, filename)
watermark_image = current_img

window.mainloop()
