import tkinter as tk
from tkinter import ttk

def add_to_selection(event):
    widget = event.widget
    item = widget.find_closest(event.x, event.y)
    item_text = widget.itemcget(item, "text")
    selected_listbox.insert(tk.END, item_text)

def remove_from_selection(event):
    selected_index = selected_listbox.nearest(event.y)
    selected_listbox.delete(selected_index)

def on_drag_start(event):
    widget = event.widget
    item = widget.find_closest(event.x, event.y)
    item_text = widget.itemcget(item, "text")
    widget.drag_data = {"item": item, "x": event.x, "y": event.y, "text": item_text}

def on_drag_motion(event):
    widget = event.widget
    x, y = event.x, event.y
    widget.move(widget.drag_data["item"], x - widget.drag_data["x"], y - widget.drag_data["y"])
    widget.drag_data["x"] = x
    widget.drag_data["y"] = y

def on_drag_end(event):
    widget = event.widget
    item = widget.drag_data["item"]
    item_text = widget.drag_data["text"]
    x, y = widget.canvasx(event.x), widget.canvasy(event.y)
    canvas_right.create_text(x, y, anchor="w", text=item_text, font=("Helvetica", 12))
    del widget.drag_data

def update_list(event):
    category = category_combobox.get()
    # Your update_list implementation goes here

def update_canvas(items):
    canvas_left.delete("all")
    y_offset = 10
    for item in items:
        canvas_left.create_text(10, y_offset, anchor="w", text=item, font=("Helvetica", 12))
        y_offset += 25
    canvas_left.config(scrollregion=canvas_left.bbox("all"))

root = tk.Tk()
root.title("Multiple Selection Combobox")

# Define available items
programming_languages = ["C#", "Java", "JavaScript"," Python", "PHP", "Kotlin", "Swift", "C++", "Bash", "R", "SQL"]
frameworks_and_libraries = ["NET", "Unity", "TensorFlow", "Keras", "React Native"," Xamarin", "Angular", "Node.js", "React", "Flask", "D3.js", "OpenCV"]
mobile_development = ["Android Development", "iOS Development (Swift, Kotlin)", "React Native", "Xamarin", "Mobile Development Best Practices", "Flutter", "HealthKit", "CareKit"]
web_development = ["HTML", "CSS", "JavaScript", "SEO Tools", "Web Development", "Web Scraping", "Web Crawling", "HTML5", "CSS3", "Drupal", "WordPress"]
ui_ux_design = ["Sketch", "Figma", "Adobe XD", "User Interface Design", "User Experience Design", "UI/UX Design"]
game_development = ["Unity", "Game Design Principles"]
software_engineering = ["Software Maintenance", "Enterprise Architecture", "Algorithm Design", "Application Development", "System Integration", "Application Design"]
cloud_computing = ["AWS", "Azure", "Cloud Computing Fundamentals", "Serverless Architecture", "Cloud Storage Solutions"]
security = ["Cybersecurity", "Encryption", "SSL", "Payment Processing APIs", "Network Security", "Ethical Hacking", "Data Security", "Information Security", "Authentication", "Biometric Identification"]
data_science_and_analytics = ["Machine Learning", "Data Analysis", "Big Data Analytics", "Data Analytics", "Data Visualization", "Data Science", "Statistical Analysis", "Predictive Modeling", "Fraud Detection Algorithms", "Health Informatics", "Quantitative Analysis", "Financial Modeling", "Statistics"]
database_management = ["Database Management", "MySQL", "MongoDB", "Oracle", "SQL Optimization", "Database Management", "Performance Tuning"]
development_tools = ["Docker", "Kubernetes", "Selenium", "Test Automation Frameworks", "Version Control", "CI/CD Pipelines"]
blockchain =["Solidity", "Ethereum", "Smart Contracts", "Blockchain Concepts", "DApp Development"]
Iot =["IoT Platforms", "IoT Integration", "Sensor Networks", "Arduino", "Raspberry Pi"]
AI_and_Robotics = ["AI Principles", "Machine Learning Algorithms", "Robotics", "Embedded Systems", "AI Concepts", "Computer Vision", "Image Processing", "Speech Recognition Libraries", "NLP Techniques", "Chatbot Frameworks"]
VR_AR = ["VR SDKs"]
graphics_design = ["Adobe Suite", "Blender", "Maya", "3D Graphics"]
user_interface =["Sketch", "Figma", "Adobe XD"]
project_management = ["Project Management Methodologies", "Agile", "Scrum", "Analytical Skills", "Team Collaboration", "Leadership"]
business_skills = ["Market Research", "Customer Behavior","Market Analysis", "Strategic Planning", "Business Strategy", "Operational Efficiency", "Financial Planning", "Fundraising Strategies", "Competitive Intelligence", "Strategic Analysis", "Product Development", "Creativity"]
regulatory_compliance = ["Legal Knowledge", "Ethical Decision Making", "Regulatory Compliance", "Environmental Law", "Data Protection Policies", "Banking and Finance Knowledge"]
sustainability = ["Sustainability Planning", "Environmental Science", "Sustainability Strategies"]
networking = ["Networking", "Socket Programming", "Multi-thread Programming"]
systems = ["Satellite Systems", "Communication Theory", "Signal Processing", "Circuit Analysis", "Circuit Design", "Soldering", "Energy Systems", "Mechanical Analysis"]
realestate = ["Real Estate Knowledge"]
communication =["Interpersonal Communication", "Active Listening", "Customer Service", "Empathy", "Communication Skills"]
management_and_leadership = ["Organizational Development", "Leadership", "Employee Motivation Techniques", "Feedback Mechanisms", "Constructive Criticism", "Team Management", "Change Management"]
personal_development = ["Time Management", "Stress Management", "Self-Discipline", "Self-Motivation Techniques", "Continuous Learning", "Adaptability"]
legal_and_ethical = ["Legal Knowledge", "Ethical Decision Making"]
Technical_proficiency = ["Technical Skills", "Technical Adaptability"]
Digital_collaboration = ["Digital Collaboration Tools"]

# Create category dropdown
categories = [
    "Programming Languages", "Frameworks and Libraries", "Mobile Development", "Web Development",
    "UI/UX Design", "Game Development", "Software Engineering", "Cloud Computing", "Security",
    "Data Science and Analytics", "Database Management", "Development Tools", "Blockchain", "Internet of Things (IoT)",
    "AI and Robotics", "Virtual Reality and Augmented Reality (VR/AR)", "Graphics Design", "User Interface",
    "Project Management", "Business Skills", "Regulatory Compliance", "Sustainability", "Networking",
    "Systems", "Real Estate", "Communication", "Management and Leadership", "Personal Development",
    "Legal and Ethical", "Technical Proficiency", "Digital Collaboration"
]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.pack(pady=10)
category_combobox.bind("<<ComboboxSelected>>", update_list)

# Frame for available options
available_frame = ttk.LabelFrame(root, text="Available Options")
available_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create left canvas for available options
canvas_left = tk.Canvas(available_frame, bg="white", highlightthickness=0)
canvas_left.pack(fill=tk.BOTH, expand=True)
canvas_left.bind("<Button-1>", on_drag_start)
canvas_left.bind("<B1-Motion>", on_drag_motion)
canvas_left.bind("<ButtonRelease-1>", on_drag_end)

# Create a frame to contain the items inside the left canvas
frame_left = tk.Frame(canvas_left, bg="white")
canvas_left.create_window((0, 0), window=frame_left, anchor="nw")

# Bind the left canvas to the frame size
def on_frame_left_configure(event):
    canvas_left.configure(scrollregion=canvas_left.bbox("all"))
frame_left.bind("<Configure>", on_frame_left_configure)

# Frame for selected options
selected_frame = ttk.LabelFrame(root, text="Selected Options")
selected_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Right canvas for selected options
canvas_right = tk.Canvas(selected_frame, bg="white", highlightthickness=0)
canvas_right.pack(fill=tk.BOTH, expand=True)

# Create a frame to contain the items inside the right canvas
frame_right = tk.Frame(canvas_right, bg="white")
canvas_right.create_window((0, 0), window=frame_right, anchor="nw")

# Bind the right canvas to the frame size
def on_frame_right_configure(event):
    canvas_right.configure(scrollregion=canvas_right.bbox("all"))
frame_right.bind("<Configure>", on_frame_right_configure)

root.mainloop()

