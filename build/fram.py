import tkinter as tk

scrollable_frame_height = 0

def add_frame():
    global scrollable_frame_height
    new_frame = tk.Frame(canvas_frame, bg="white", width=200, height=50)
    new_frame.pack(fill=tk.X)
    canvas.create_window((0, scrollable_frame_height), window=new_frame, anchor="nw")
    scrollable_frame_height += 50  # Adjust this value based on the height of each frame

root = tk.Tk()
root.geometry("300x200")

# Create a canvas widget
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to contain the scrollable content
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Add some frames
for _ in range(10):
    add_frame()

# Update the scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
