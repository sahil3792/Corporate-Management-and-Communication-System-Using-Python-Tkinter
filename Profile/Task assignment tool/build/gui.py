
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Documents\Projects\Major Project\Skive\NewDirectory\Profile\Task assignment tool\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("510x450")
window.configure(bg = "#3A868F")


canvas = Canvas(
    window,
    bg = "#3A868F",
    height = 450,
    width = 510,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    255.0,
    225.0,
    image=image_image_1
)

canvas.create_rectangle(
    17.0,
    11.0,
    493.0,
    165.0,
    fill="#225777",
    outline="")

canvas.create_text(
    35.0,
    26.0,
    anchor="nw",
    text="Task Assignment Tool",
    fill="#ECECD9",
    font=("Libre Caslon Text", 19 * -1)
)

canvas.create_text(
    35.0,
    71.0,
    anchor="nw",
    text="Choose Document \nfrom Files:-",
    fill="#FFFFFF",
    font=("Libre Caslon Text", 14 * -1)
)

canvas.create_text(
    35.0,
    113.0,
    anchor="nw",
    text="Skills Required :-",
    fill="#FFFFFF",
    font=("Libre Caslon Text", 14 * -1)
)

canvas.create_text(
    159.0,
    113.0,
    anchor="nw",
    text="Python,Java,etc",
    fill="#FFFFFF",
    font=("Libre Caslon Text", 14 * -1)
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
    x=199.0,
    y=71.0,
    width=192.0,
    height=36.0
)

canvas.create_rectangle(
    17.0,
    181.0,
    493.0,
    433.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    33.0,
    197.0,
    479.0,
    278.0,
    fill="#173054",
    outline="")

canvas.create_rectangle(
    33.0,
    284.0,
    479.0,
    365.0,
    fill="#173054",
    outline="")
window.resizable(False, False)
window.mainloop()
