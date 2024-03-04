import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hp\Downloads\Corporate-Management-and-Communication-System-Using-Python-Tkinter-main\Corporate-Management-and-Communication-System-Using-Python-Tkinter-main\Profile\SkillsPage\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_configure(event):
    Optioncanvas.configure(scrollregion=Optioncanvas.bbox("all"))

def update_list(event):
    category = category_combobox.get()
    update_canvas(get_items_by_category(category))

def update_canvas(items):
    Optioncanvas.delete("all")
    y_offset = 10
    for item in items:
        Optioncanvas.create_text(10, y_offset, anchor="w", text=item, font=("Helvetica", 12))
        y_offset += 25
    Optioncanvas.config(scrollregion=Optioncanvas.bbox("all"))

def get_items_by_category(category):
    # Define items for each category here
    items = {
        "Programming Languages": ["C#", "Java", "JavaScript", "Python", "PHP", "Kotlin", "Swift", "C++", "Bash", "R", "SQL"],
        "Frameworks and Libraries": ["NET", "Unity", "TensorFlow", "Keras", "React Native", "Xamarin", "Angular", "Node.js", "React", "Flask", "D3.js", "OpenCV"],
        # Add more categories and items as needed
    }
    return items.get(category, [])

window = tk.Tk()
window.title("Multiple Selection Combobox")
window.geometry("700x450")
window.configure(bg="#173054")

canvas = tk.Canvas(
    window,
    bg="#173054",
    height=450,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(350.0, 225.0, image=image_image_1)

canvas.create_text(
    162.0,
    34.0,
    anchor="nw",
    text="Choose Your Skill :",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 17 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(472.5, 44.5, image=entry_image_1)

categories = ["Programming Languages", "Frameworks and Libraries"]  # Add more categories here
category_combobox = ttk.Combobox(canvas, values=categories)
category_combobox.place(x=351, y=30, width=244, height=30)
category_combobox.bind("<<ComboboxSelected>>", update_list)

canvas_frame = ttk.Frame(window, width=303.0, height=253.0)
canvas_frame.place(x=26.0, y=103.0)

Optioncanvas = tk.Canvas(window, bg="white", highlightthickness=0)
Optioncanvas.place(x=26, y=103, height=253, width=300)

vsb = tk.Scrollbar(Optioncanvas, orient="vertical", command=Optioncanvas.yview)
vsb.pack(side="right", fill="y")
Optioncanvas.config(yscrollcommand=vsb.set)

Optioncanvas.bind("<Configure>", on_configure)

listbox_frame = ttk.Frame(window, width=303, height=253)
listbox_frame.place(x=374, y=103)

selected_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE)
selected_listbox.place(x=0, y=0, width=303, height=253)

vsb_listbox = tk.Scrollbar(selected_listbox, orient="vertical", command=selected_listbox.yview)
vsb_listbox.place(x=374, y=103)
selected_listbox.config(yscrollcommand=vsb_listbox.set)

window.mainloop()
