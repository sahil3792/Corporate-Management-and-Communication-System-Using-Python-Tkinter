import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Text Editor")

text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

bold_mode = False

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def bold_text():
    global bold_mode
    bold_mode = not bold_mode

def on_key_press(event):
    if bold_mode:
        text_area.tag_configure("bold", font=("TkDefaultFont", 11, "bold"))
        text_area.insert(tk.END, event.char)
        text_area.tag_add("bold", "end - 1c", tk.END)

text_area.bind("<KeyPress>", on_key_press)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", command=text_area.edit_redo)
menubar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menubar)

toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

bold_button = tk.Button(toolbar, text="Bold", command=bold_text)
bold_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
