'''import tkinter as tk
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
'''

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from pymongo import MongoClient
from datetime import datetime

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from pymongo import MongoClient
from datetime import datetime

def add_task_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Task")

    def submit_task():
        selected_date = cal.get_date()
        selected_hour = hour_var.get()
        selected_minute = minute_var.get()
        task = task_entry.get()

        if selected_date and selected_hour and selected_minute and task:
            datetime_str = f"{selected_date} {selected_hour}:{selected_minute}"
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

            task_data = {
                "username": username,
                "company": company,
                "date": datetime_obj,
                "task": task
            }

            collection.insert_one(task_data)
            print("Task added successfully.")

            add_window.destroy()
            display_tasks()

        else:
            print("Please fill in all fields.")

    cal = Calendar(add_window, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=10)

    hour_label = tk.Label(add_window, text="Due Time (HH:MM):")
    hour_label.pack()
    
    hour_var = tk.StringVar(add_window)
    hour_dropdown = ttk.Combobox(add_window, textvariable=hour_var)
    hour_dropdown['values'] = tuple(str(i).zfill(2) for i in range(24))
    hour_dropdown.current(0)  # Default value
    hour_dropdown.pack()

    minute_var = tk.StringVar(add_window)
    minute_dropdown = ttk.Combobox(add_window, textvariable=minute_var)
    minute_dropdown['values'] = tuple(str(i).zfill(2) for i in range(60))
    minute_dropdown.current(0)  # Default value
    minute_dropdown.pack()

    task_label = tk.Label(add_window, text="Task:")
    task_label.pack()
    task_entry = tk.Entry(add_window)
    task_entry.pack()

    submit_button = tk.Button(add_window, text="Submit", command=submit_task)
    submit_button.pack()

def delete_task(task_id, task_label, date_label, tasks_dict):
    collection.delete_one({"_id": task_id})
    task_label.destroy()

    tasks_dict[date_label["text"]].remove(task_id)
    if not tasks_dict[date_label["text"]]:
        date_label.destroy()

def display_tasks():
    global tasks_frame

    if 'tasks_frame' in globals():
        tasks_frame.destroy()

    tasks_frame = tk.Frame(root)
    tasks_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    tasks = collection.find().sort("date", 1)
    tasks_dict = {}
    for task in tasks:
        task_date = task["date"].strftime("%d %B %Y")
        if task_date not in tasks_dict:
            tasks_dict[task_date] = []

        tasks_dict[task_date].append(task["_id"])

    for date_label_text, task_ids in tasks_dict.items():
        date_label = tk.Label(tasks_frame, text=date_label_text)
        date_label.pack(anchor="w", pady=5)

        for task_id in task_ids:
            task = collection.find_one({"_id": task_id})
            task_details = f"{task['task']}  {task['date'].strftime('%H:%M')}"
            task_label = tk.Label(tasks_frame, text=task_details, cursor="hand2", fg="blue")
            task_label.pack(side=tk.LEFT, anchor="w")
            task_label.bind("<Button-1>", lambda event, id=task_id, label=task_label, date_label=date_label, tasks_dict=tasks_dict: delete_task(id, label, date_label, tasks_dict))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Todo List Application")

    username = "user123"  # Replace with actual username
    company = "example company"  # Replace with actual company name

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    add_button = tk.Button(frame, text="Add Task", command=add_task_window)
    add_button.pack()

    client = MongoClient("mongodb://localhost:27017/")
    db = client["TodoListDB"]
    collection = db["TodoListCollection"]

    tasks_frame = tk.Frame(root)
    tasks_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    display_tasks()

    root.mainloop()





