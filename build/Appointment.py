import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from datetime import datetime

class AppointmentScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Scheduler")

        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['appointment_scheduler']
        self.collection = self.db['appointments']

        self.create_widgets()

    def create_widgets(self):
        self.reason_label = tk.Label(self.root, text="Reason:")
        self.reason_label.pack()
        self.reason_entry = tk.Entry(self.root)
        self.reason_entry.pack()

        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        self.time_label = tk.Label(self.root, text="Time (HH:MM):")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()

        self.submit_button = tk.Button(self.root, text="Schedule Appointment", command=self.submit_appointment)
        self.submit_button.pack()

        self.view_button = tk.Button(self.root, text="View Appointments", command=self.view_appointments)
        self.view_button.pack()

    def validate_datetime(self, date_str, time_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            datetime.strptime(time_str, "%H:%M")
            return True
        except ValueError:
            return False

    def submit_appointment(self):
        reason = self.reason_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if not reason or not date or not time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not self.validate_datetime(date, time):
            messagebox.showerror("Error", "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            return

        appointment = {
            'reason': reason,
            'date': date,
            'time': time
        }
        self.collection.insert_one(appointment)
        messagebox.showinfo("Success", "Appointment scheduled successfully.")

    def view_appointments(self):
        appointments = self.collection.find()
        if appointments.count() == 0:
            messagebox.showinfo("No Appointments", "No appointments scheduled yet.")
        else:
            appointment_list = "\n".join([f"Reason: {app['reason']}, Date: {app['date']}, Time: {app['time']}" for app in appointments])
            messagebox.showinfo("Appointments", appointment_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentScheduler(root)
    root.mainloop()
