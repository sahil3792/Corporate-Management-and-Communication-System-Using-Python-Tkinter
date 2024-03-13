import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar  # Install tkcalendar via pip: pip install tkcalendar
from datetime import datetime
import pymongo
from bson.objectid import ObjectId

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
employee_collection = db["employeecollection"]

def add_task():
    def submit_task():
        due_date = due_date_calendar.get_date()
        due_time = f"{hours_var.get()}:{minutes_var.get()}"
        task = task_entry.get()
        username = "UserName"  # You should replace "UserName" with the actual username

        if due_date and task:
            task_data = {
                "_id": str(ObjectId()),
                "username": username,
                "due_date": due_date,
                "due_time": due_time,
                "task_details": task
            }
            employee_collection.insert_one(task_data)
            new_window.destroy()
            display_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter both due date and task details.")

    new_window = tk.Toplevel(root)
    new_window.title("Add Task")

    due_date_label = tk.Label(new_window, text="Due Date:")
    due_date_label.grid(row=0, column=0, padx=10, pady=5)

    due_date_calendar = Calendar(new_window, selectmode="day",
                                  year=datetime.now().year, month=datetime.now().month,
                                  day=datetime.now().day)
    due_date_calendar.grid(row=0, column=1, padx=10, pady=5)

    time_frame = ttk.Frame(new_window)
    time_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    hours_var = tk.StringVar()
    hours_label = tk.Label(time_frame, text="Hours:")
    hours_label.grid(row=0, column=0, padx=5, pady=5)
    hours_dropdown = ttk.Combobox(time_frame, textvariable=hours_var, values=[str(i).zfill(2) for i in range(24)])
    hours_dropdown.current(0)
    hours_dropdown.grid(row=0, column=1, padx=5, pady=5)

    minutes_var = tk.StringVar()
    minutes_label = tk.Label(time_frame, text="Minutes:")
    minutes_label.grid(row=0, column=2, padx=5, pady=5)
    minutes_dropdown = ttk.Combobox(time_frame, textvariable=minutes_var, values=[str(i).zfill(2) for i in range(60)])
    minutes_dropdown.current(0)
    minutes_dropdown.grid(row=0, column=3, padx=5, pady=5)

    task_label = tk.Label(new_window, text="Task:")
    task_label.grid(row=2, column=0, padx=10, pady=5)
    task_entry = tk.Entry(new_window)
    task_entry.grid(row=2, column=1, padx=10, pady=5)

    submit_button = tk.Button(new_window, text="Submit", command=submit_task)
    submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

def display_tasks():
    username = "UserName"  # You should replace "UserName" with the actual username
    tasks = employee_collection.find({"username": username}).sort([("due_date", pymongo.ASCENDING), ("due_time", pymongo.ASCENDING)])
    for task in tasks:
        task_info = f"{task['due_date']} {task['due_time']}: {task['task_details']}"
        task_label = tk.Label(root, text=task_info)
        task_label.pack(padx=5, pady=5)

root = tk.Tk()
root.title("To-Do List")

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=10)

display_tasks()

root.mainloop()
