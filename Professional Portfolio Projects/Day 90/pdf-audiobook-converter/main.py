from tkinter import *
from tkinter import filedialog as fd
from text2speech import text_to_speech
from pdfminer.high_level import extract_text

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
BG_COLOR = '#856ff8'


class Gui:
    def __init__(self):
        self.pdf_path = None
        self.text = None
        self.window = Tk()
        self.window.title('WATERMARK IT')
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(padx=100, pady=50, bg=BG_COLOR)

        self.top_frame = Frame(self.window, bg=BG_COLOR, padx=20)
        self.top_frame.grid(column=1, row=0, sticky='NW')

        self.file_btn = Button(self.top_frame, text="Select a PDF", command=self.select_file, font=(FONT_NAME, 18),
                               highlightthickness=0, width=25)
        self.file_btn.grid(column=0, row=0, sticky='W')
        self.file_label = Label(self.top_frame, text="Uploaded: N/A", bg=BG_COLOR, font=(FONT_NAME, 18), pady=10, wraplength=275,
                                justify='left')
        self.file_label.grid(column=0, row=1, sticky='W')
        self.download_btn = Button(self.top_frame, state='disabled', text="Download MP3", command=self.download,
                                   font=(FONT_NAME, 18), highlightthickness=0, width=25)
        self.download_btn.grid(column=0, row=2, sticky='W')
        self.reset_btn = Button(self.top_frame, state='disabled', text="Reset", command=self.reset,
                                   font=(FONT_NAME, 18), highlightthickness=0, width=25)
        self.reset_btn.grid(column=0, row=3, sticky='W', pady=30)

    def update_file_label(self, file_path):
        self.file_label.config(text=f"Uploaded: {file_path.split('/')[-1]}")

    def select_file(self):
        self.pdf_path = fd.askopenfilename()
        self.update_file_label(self.pdf_path)
        self.text = extract_text(self.pdf_path)
        self.download_btn.config(state='active')

    def download(self):
        pdf_name = self.pdf_path.split('/')[-1].split('.pdf')[0]
        text_to_speech(self.text, pdf_name)
        self.file_label.config(text="Success! MP3 downloaded!")
        self.download_btn.config(state='disabled')
        self.reset_btn.config(state='active')
        self.file_btn.config(state='disabled')

    def reset(self):
        self.pdf_path = None
        self.text = None
        self.file_label.config(text="Uploaded: N/A")
        self.reset_btn.config(state='disabled')
        self.file_btn.config(state='active')


if __name__ == "__main__":
    gui = Gui()
    gui.window.mainloop()
