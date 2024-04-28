
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hp\Documents\Projects\Corporate-Management-and-Communication-System-Using-Python-Tkinter\Profile\FileUploadGUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("510x450")
window.configure(bg = "#173054")


canvas = Canvas(
    window,
    bg = "#173054",
    height = 450,
    width = 510,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    21.0,
    7.0,
    anchor="nw",
    text="Files",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=383.0,
    y=13.0,
    width=106.0,
    height=36.0
)

canvas.create_rectangle(
    21.0,
    60.0,
    489.0,
    91.0,
    fill="#3A868F",
    outline="")

canvas.create_text(
    30.0,
    68.0,
    anchor="nw",
    text="File Name",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 17 * -1)
)
window.resizable(False, False)
window.mainloop()
