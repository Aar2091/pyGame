from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk()
window.title("Aarav's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def open_file():

    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")
    ])

    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "r") as input_file:

        text = input_file.read()

        txt_edit.intersect(END, text)
        input_file.close()

window.title(f"Aarav's text editor - {filepath}")