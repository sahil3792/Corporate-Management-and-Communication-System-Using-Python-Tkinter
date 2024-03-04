import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
from calendar import monthrange
from collections import defaultdict
root = tk.Tk()

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar with To-Do List")
        self.root.geometry("700x500")
        self.root.configure(bg="#ECECD9")

        self.tasks = defaultdict(list)
        self.current_date = datetime.now()
        self.initialize_calendar()

    def initialize_calendar(self):
        self.label = tk.Label(self.root, text=self.current_date.strftime('%B %Y'), font=("Arial", 18, "bold"), bg="#ECECD9")
        self.label.pack(fill=tk.X, pady=10)

        self.days_frame = tk.Frame(self.root, bg="#ECECD9")
        self.days_frame.pack()

        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for day in days_of_week:
            label = tk.Label(self.days_frame, text=day, font=("Arial", 12), width=8, bg="#ECECD9")
            label.grid(row=0, column=days_of_week.index(day))

        self.calendar_frame = tk.Frame(self.root, bg="#ECECD9")
        self.calendar_frame.pack(pady=10)

        self.task_box = tk.Listbox(self.root, width=60, height=10, font=("Arial", 12), selectbackground="#225777", selectforeground="#ECECD9", bg="#ECECD9")
        self.task_box.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#ECECD9")
        button_frame.pack()

        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, bg="#3A868F", fg="#ECECD9", font=("Arial", 12))
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.complete_button = tk.Button(button_frame, text="Mark as Completed", command=self.mark_as_completed, bg="#3A868F", fg="#ECECD9", font=("Arial", 12))
        self.complete_button.pack(side=tk.LEFT)

        self.remove_button = tk.Button(button_frame, text="Remove Task", command=self.remove_task, bg="#3A868F", fg="#ECECD9", font=("Arial", 12))
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.update_calendar()

    def update_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        month, year = self.current_date.month, self.current_date.year
        cal = self.get_month(month, year)

        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                day_frame = tk.Frame(self.calendar_frame, height=40, width=80, bg="#ECECD9")
                day_frame.grid(row=i, column=j)

                day_label = tk.Label(day_frame, text=str(day) if day != 0 else "", font=("Arial", 14), bg="#ECECD9")
                day_label.pack(padx=5, pady=2)

                day_frame.bind("<Button-1>", lambda event, day=day: self.show_tasks(day))
        
    def show_tasks(self, day):
        task_date = datetime(self.current_date.year, self.current_date.month, day)
        tasks = self.tasks.get((task_date.year, task_date.month, task_date.day), [])
        self.task_box.delete(0, tk.END)
        for task in tasks:
            self.task_box.insert(tk.END, task)

    def get_month(self, month, year):
        cal = []
        month_calendar = [[0]*7 for _ in range(6)]
        days_in_month = monthrange(year, month)[1]

        first_day = datetime(year, month, 1).weekday()  # 0 = Monday, 6 = Sunday
        day_counter = 1

        for i in range(6):
            for j in range(7):
                if i == 0 and j < first_day:
                    month_calendar[i][j] = 0
                elif day_counter <= days_in_month:
                    month_calendar[i][j] = day_counter
                    day_counter += 1

        return month_calendar

    def add_task(self):
        task_description = simpledialog.askstring("Input", "Enter task description:")
        if task_description:
            self.tasks[(self.current_date.year, self.current_date.month, self.current_date.day)].append("[ ] " + task_description)
            self.show_tasks(self.current_date.day)

    def mark_as_completed(self):
        selected_task_index = self.task_box.curselection()
        if selected_task_index:
            task_index = int(selected_task_index[0])
            task_date = self.current_date
            task_list = self.tasks[(task_date.year, task_date.month, task_date.day)]
            if 0 <= task_index < len(task_list):
                task = task_list[task_index]
                if "[ ]" in task:
                    task_list[task_index] = task.replace("[ ]", "[✔️]")
                    self.show_tasks(self.current_date.day)
        else:
            messagebox.showwarning("Warning", "No task selected.")

    def remove_task(self):
        selected_task_index = self.task_box.curselection()
        if selected_task_index:
            task_index = int(selected_task_index[0])
            task_date = self.current_date
            task_list = self.tasks[(task_date.year, task_date.month, task_date.day)]
            if 0 <= task_index < len(task_list):
                del task_list[task_index]
                self.show_tasks(self.current_date.day)
        else:
            messagebox.showwarning("Warning", "No task selected.")
app = CalendarApp(root)

root.mainloop()
