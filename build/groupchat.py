import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
from tkinter import messagebox


# Connection String to connect to the MongoDB Atlas
conn_str = "mongodb+srv://root:812003@cluster0.fshfquh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(conn_str)

# Accessing the EmployeeCollection
employee_collection = client["EmployeeDatabase"]["EmployeeCollection"]

# Function to search for employees by UserName
def search_employees(username):
    regex = f"^{username}"
    employees = employee_collection.find({"UserName": {"$regex": regex}})
    return [employee["UserName"] for employee in employees]

# Function to handle clicking on the "Create Group" button
def create_group():
    group_name = group_name_entry.get()
    selected_usernames = search_dropdown.get()
    if selected_usernames:
        selected_users_listbox.insert(tk.END, selected_usernames)
        search_entry.delete(0, tk.END)
        search_dropdown.set('')
    else:
        messagebox.showerror("Error", "Please select a user from the dropdown.")

# Function to handle selection from the autocomplete dropdown
def on_select_from_dropdown(event):
    selected_usernames = search_dropdown.get()
    if selected_usernames:
        selected_users_listbox.insert(tk.END, selected_usernames)
        search_entry.delete(0, tk.END)
        search_dropdown.set('')
    else:
        messagebox.showerror("Error", "Please select a user from the dropdown.")

# Function to handle changes in the search entry field
def on_search_entry_changed(*args):
    search_text = search_var.get()
    matches = search_employees(search_text)
    search_dropdown.configure(values=matches)
    search_dropdown.place(x=search_entry.winfo_x(), y=search_entry.winfo_y() + search_entry.winfo_height())

# GUI Setup
root = tk.Tk()
root.title("Group Chat Application")

# Main frame
main_frame = tk.Frame(root, width=510, height=450)
main_frame.pack()

# Left frame for group chat label and create group button
left_frame = tk.Frame(main_frame, width=100, height=450)
left_frame.grid(row=0, column=0)

group_chat_label = tk.Label(left_frame, text="Group Chat")
group_chat_label.pack(pady=10)

create_group_button = tk.Button(left_frame, text="Create Group", command=create_group)
create_group_button.pack(pady=10)

# Right frame for group creation
right_frame = tk.Frame(main_frame, width=410, height=450)
right_frame.grid(row=0, column=1)

# Entry field for entering the group name
group_name_label = tk.Label(right_frame, text="Enter Group Name:")
group_name_label.pack(pady=10)

group_name_entry = tk.Entry(right_frame, width=40)
group_name_entry.pack(pady=10)

# Search bar for searching employees
search_label = tk.Label(right_frame, text="Search Employee:")
search_label.pack(pady=10)

search_var = tk.StringVar()
search_var.trace("w", on_search_entry_changed)
search_entry = tk.Entry(right_frame, width=40, textvariable=search_var)
search_entry.pack(pady=10)

search_dropdown = ttk.Combobox(right_frame, width=38)
search_dropdown.bind("<<ComboboxSelected>>", on_select_from_dropdown)
search_dropdown.bind("<FocusOut>", lambda event: search_dropdown.place_forget())

# Selected users list
selected_users_var = tk.StringVar()
selected_users_label = tk.Label(right_frame, text="Selected Users:")
selected_users_label.pack(pady=10)

selected_users_listbox = tk.Listbox(right_frame, width=40, height=10, listvariable=selected_users_var, selectmode="multiple")
selected_users_listbox.pack(pady=10)

root.mainloop()
