import tkinter as tk
from tkinter import messagebox

# Employee database (in real-world scenario, this could be a MongoDB or SQL database)
employee_db = {
    "Sahil S.": {"password": "123", "status": "pending"},
    "employee2": {"password": "password2", "status": "pending"},
    "employee3": {"password": "password3", "status": "pending"}
}

# Admin login
admin_username = "admin"
admin_password = "adminpass"

def login_employee():
    username = username_entry.get()
    password = password_entry.get()

    if username in employee_db:
        employee = employee_db[username]
        if employee["password"] == password:
            if employee["status"] == "approved":
                messagebox.showinfo("Login Success", "Employee login approved!")
            elif employee["status"] == "rejected":
                messagebox.showerror("Login Error", "Employee login request rejected by admin.")
            else:
                messagebox.showinfo("Login Pending", "Employee login request is pending approval.")
        else:
            messagebox.showerror("Login Error", "Incorrect password.")
    else:
        messagebox.showerror("Login Error", "Employee not found.")

def admin_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == admin_username and password == admin_password:
        # Open admin interface
        admin_window = tk.Toplevel(root)
        admin_window.title("Admin Interface")
        admin_window.geometry("300x200")

        # Listbox to display pending login requests
        pending_listbox = tk.Listbox(admin_window)
        pending_listbox.pack(pady=10)

        # Function to approve login request
        def approve_login():
            selected_employee = pending_listbox.get(tk.ACTIVE)
            employee_db[selected_employee]["status"] = "approved"
            messagebox.showinfo("Approval", f"Login request for {selected_employee} approved.")

        # Button to approve login request
        approve_button = tk.Button(admin_window, text="Approve", command=approve_login)
        approve_button.pack(pady=5)

        # Populate listbox with pending login requests
        for employee, data in employee_db.items():
            if data["status"] == "pending":
                pending_listbox.insert(tk.END, employee)
    else:
        messagebox.showerror("Admin Login Error", "Incorrect admin credentials.")

# Main Tkinter window
root = tk.Tk()
root.title("Employee Login")
root.geometry("300x150")

# Username and password entry fields
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Button for employee login
employee_login_button = tk.Button(root, text="Employee Login", command=login_employee)
employee_login_button.pack(pady=5)

# Button for admin login
admin_login_button = tk.Button(root, text="Admin Login", command=admin_login)
admin_login_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
