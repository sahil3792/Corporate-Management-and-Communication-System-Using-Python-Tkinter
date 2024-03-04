import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def browse_photo():
    filename = filedialog.askopenfilename(title="Select Photo", filetypes=(("Image files", "*.jpg; *.jpeg; *.png"), ("All files", "*.*")))
    if filename:
        image = Image.open(filename)
        image = image.resize((150, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        photo_label.config(image=photo)
        photo_label.image = photo

def submit_form():
    first_name = first_name_entry.get()
    middle_name = middle_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    address = address_entry.get("1.0", "end-1c")
    mobile_number = mobile_number_entry.get()
    birthdate = birthdate_entry.get()
    skills = skills_entry.get("1.0", "end-1c")
    education = education_entry.get("1.0", "end-1c")
    work_experience = work_experience_entry.get("1.0", "end-1c")
    previous_salary = previous_salary_entry.get()

    print("First Name:", first_name)
    print("Middle Name:", middle_name)
    print("Last Name:", last_name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Mobile Number:", mobile_number)
    print("Birthdate:", birthdate)
    print("Skills:", skills)
    print("Education:", education)
    print("Work Experience:", work_experience)
    print("Previous Salary:", previous_salary)

window = tk.Tk()
window.title("User Data Form")

# Create form labels and entry widgets
tk.Label(window, text="First Name:").grid(row=0, column=0, sticky="w")
first_name_entry = tk.Entry(window)
first_name_entry.grid(row=0, column=1)

tk.Label(window, text="Middle Name:").grid(row=1, column=0, sticky="w")
middle_name_entry = tk.Entry(window)
middle_name_entry.grid(row=1, column=1)

tk.Label(window, text="Last Name:").grid(row=2, column=0, sticky="w")
last_name_entry = tk.Entry(window)
last_name_entry.grid(row=2, column=1)

tk.Label(window, text="Age:").grid(row=3, column=0, sticky="w")
age_entry = tk.Entry(window)
age_entry.grid(row=3, column=1)

tk.Label(window, text="Gender:").grid(row=4, column=0, sticky="w")
gender_combobox = ttk.Combobox(window, values=["Male", "Female", "Other"])
gender_combobox.grid(row=4, column=1)

tk.Label(window, text="Address:").grid(row=5, column=0, sticky="w")
address_entry = tk.Text(window, height=4, width=30)
address_entry.grid(row=5, column=1)

tk.Label(window, text="Mobile Number:").grid(row=6, column=0, sticky="w")
mobile_number_entry = tk.Entry(window)
mobile_number_entry.grid(row=6, column=1)

tk.Label(window, text="Birthdate:").grid(row=7, column=0, sticky="w")
birthdate_entry = tk.Entry(window)
birthdate_entry.grid(row=7, column=1)

tk.Label(window, text="Skills:").grid(row=8, column=0, sticky="w")
skills_entry = tk.Text(window, height=4, width=30)
skills_entry.grid(row=8, column=1)

tk.Label(window, text="Education:").grid(row=9, column=0, sticky="w")
education_entry = tk.Text(window, height=4, width=30)
education_entry.grid(row=9, column=1)

tk.Label(window, text="Work Experience:").grid(row=10, column=0, sticky="w")
work_experience_entry = tk.Text(window, height=4, width=30)
work_experience_entry.grid(row=10, column=1)

tk.Label(window, text="Previous Salary:").grid(row=11, column=0, sticky="w")
previous_salary_entry = tk.Entry(window)
previous_salary_entry.grid(row=11, column=1)

# Button to upload photo
upload_button = tk.Button(window, text="Upload Photo", command=browse_photo)
upload_button.grid(row=12, column=0, columnspan=2)

# Label to display uploaded photo
photo_label = tk.Label(window)
photo_label.grid(row=13, column=0, columnspan=2)

# Button to submit form
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=14, column=0, columnspan=2)

window.mainloop()