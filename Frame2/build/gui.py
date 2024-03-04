


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Documents\Projects\Skive\Frame2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x450")
window.configure(bg = "#ECECD9")


canvas = Canvas(
    window,
    bg = "#ECECD9",
    height = 450,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    225.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    350.0,
    67.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    350.0,
    142.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=280.0,
    y=132.0,
    width=140.0,
    height=19.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    350.0,
    185.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=280.0,
    y=175.0,
    width=140.0,
    height=19.0
)

canvas.create_text(
    280.0,
    119.0,
    anchor="nw",
    text="Email",
    fill="#225777",
    font=("Libre Caslon Text", 10 * -1)
)

canvas.create_text(
    280.0,
    162.0,
    anchor="nw",
    text="Password",
    fill="#225777",
    font=("Libre Caslon Text", 10 * -1)
)

canvas.create_text(
    322.0,
    96.0,
    anchor="nw",
    text="Sign In",
    fill="#225777",
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
    x=381.0,
    y=198.0,
    width=40.0,
    height=12.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=280.0,
    y=221.0,
    width=140.0,
    height=21.0
)
window.resizable(False, False)
window.mainloop()
