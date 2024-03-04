import tkinter as tk
from tkinter import Text
import tkinter.simpledialog
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import socket
import threading
import webbrowser
import re

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

def toggle_bold():
    current_tags = text.tag_names(tk.SEL_FIRST)
    if 'bold' in current_tags:
        text.tag_remove('bold', tk.SEL_FIRST, tk.SEL_LAST)
    else:
        text.tag_add('bold', tk.SEL_FIRST, tk.SEL_LAST)
        text.tag_configure('bold', font=('Helvetica', 12, 'bold'))


def toggle_italic():
    current_tags = text.tag_names(tk.SEL_FIRST)
    if 'italic' in current_tags:
        text.tag_remove('italic', tk.SEL_FIRST, tk.SEL_LAST)
    else:
        text.tag_add('italic', tk.SEL_FIRST, tk.SEL_LAST)
        text.tag_configure('italic', font=('Helvetica', 12, 'italic'))


def insert_numbered_list():
    selected_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    lines = selected_text.split('\n')
    for i, line in enumerate(lines, start=1):
        text.insert(tk.SEL_FIRST, f"{i}. {line}\n")
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)

def insert_bullet_points():
    selected_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    lines = selected_text.split('\n')
    for line in lines:
        text.insert(tk.SEL_FIRST, f"• {line}\n")
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)

def insert_html_code():
    text_content = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    html_code = f"<html>\n<head>\n</head>\n<body>\n{text_content}\n</body>\n</html>"
    text.insert(tk.SEL_FIRST, html_code)
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)


def open_url_window():
    url_window = tk.Toplevel(root)
    url_window.title("Enter URL")
    url_entry = tk.Entry(url_window)
    url_entry.pack()
    open_button = tk.Button(url_window, text="Open URL", command=lambda: webbrowser.open(url_entry.get()))
    open_button.pack()

def insert_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.gif *.ppm *.pgm *.pbm *.pgm")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)  # Convert the image to PhotoImage
        text.image_create(tk.END, image=photo)
        text.update_idletasks()

# Function to receive images from clients
def receive_image(client_socket):
    try:
        while True:
            image_bytes = client_socket.recv(1024)
            if not image_bytes:
                break
            image_data += image_bytes
        image = Image.open(io.BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)
        shared_text.image_create(tk.END, image=photo)
        shared_text.update_idletasks()
    except:
        pass

# Function to send the document to other clients
def send_document():
    selected_text = text.get("1.0", tk.END)
    for client in clients:
        client.send(selected_text.encode("utf-8"))


# Function to connect to the document sharing server
def connect_to_server():
    try:
        server_ip = server_ip_entry.get()
        server_port = int(server_port_entry.get())
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        clients.append(client_socket)
        shared_text.insert(tk.END, "Connected to the server\n")
        shared_text.update_idletasks()
        thread = threading.Thread(target=receive_image, args=(client_socket,))
        thread.start()
    except Exception as e:
        shared_text.insert(tk.END, f"Failed to connect to the server: {str(e)}\n")
        shared_text.update_idletasks()
    

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Create a text area
text = Text(root)
text.pack(fill="both", expand=True)

# Create a text area for showing server connection status
shared_text = tk.Text(root, height=5, width=50)
shared_text.pack()

# Create formatting buttons
bold_button = tk.Button(root, text="Bold", command=toggle_bold)
italic_button = tk.Button(root, text="Italic", command=toggle_italic)
numbered_list_button = tk.Button(root, text="Numbered List", command=insert_numbered_list)
bullet_points_button = tk.Button(root, text="Bullet Points", command=insert_bullet_points)
html_button = tk.Button(root, text="HTML Code", command=insert_html_code)
image_button = tk.Button(root, text="Insert Image", command=insert_image)
send_button = tk.Button(root, text="Send Document", command=send_document)
open_url_button = tk.Button(root, text="Open URL Window", command=open_url_window)

# Create entry fields for server IP and port
server_ip_label = tk.Label(root, text="Server IP:")
server_ip_label.pack()
server_ip_entry = tk.Entry(root)
server_ip_entry.pack()

server_port_label = tk.Label(root, text="Server Port:")
server_port_label.pack()
server_port_entry = tk.Entry(root)
server_port_entry.pack()

bold_button.pack(side=tk.LEFT)
italic_button.pack(side=tk.LEFT)
numbered_list_button.pack(side=tk.LEFT)
bullet_points_button.pack(side=tk.LEFT)
html_button.pack(side=tk.LEFT)
open_url_button.pack(side=tk.LEFT)
image_button.pack(side=tk.LEFT)
send_button.pack(side=tk.LEFT)

# Create a button to connect to the server
connect_button = tk.Button(root, text="Connect to Server", command=connect_to_server)
connect_button.pack()

clients = []

root.mainloop()