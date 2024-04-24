
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hp\Documents\Projects\Corporate-Management-and-Communication-System-Using-Python-Tkinter\Profile\Leave Management Application Admin Side\build\assets\frame0")


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
    66.0,
    7.0,
    anchor="nw",
    text="Leave Applications",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 18 * -1)
)

canvas.create_rectangle(
    21.0,
    60.0,
    489.0,
    118.0,
    fill="#3A868F",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    330.5,
    96.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=273.0,
    y=86.0,
    width=115.0,
    height=19.0
)

canvas.create_text(
    274.0,
    70.0,
    anchor="nw",
    text="Status",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 15 * -1)
)

canvas.create_text(
    30.0,
    68.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 17 * -1)
)

canvas.create_text(
    30.0,
    95.0,
    anchor="nw",
    text="Start Date",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 15 * -1)
)

canvas.create_text(
    140.0,
    94.0,
    anchor="nw",
    text="End Date",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 15 * -1)
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
    x=397.0,
    y=71.0,
    width=81.0,
    height=36.0
)
window.resizable(False, False)
window.mainloop()