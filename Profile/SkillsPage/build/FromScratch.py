from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hp\Downloads\Corporate-Management-and-Communication-System-Using-Python-Tkinter-main\Corporate-Management-and-Communication-System-Using-Python-Tkinter-main\Profile\SkillsPage\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_configure(event):
    # Update scroll region to encompass the full canvas
    SelectedOptionCanvas.configure(scrollregion=SelectedOptionCanvas.bbox("all"))

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
    item = widget.find_closest(event.x, event.y)
    item_text = widget.drag_data["text"]
    selected_listbox.insert(tk.END, item_text)
    del widget.drag_data



def update_list(event):
    category = category_combobox.get()
    update_canvas(get_items_by_category(category))

def update_canvas(items):
    SelectedOptionCanvas.delete("all")
    y_offset = 10
    for item in items:
        SelectedOptionCanvas.create_text(10, y_offset, anchor="w", text=item, font=("Helvetica", 12))
        y_offset += 25
    SelectedOptionCanvas.config(scrollregion=SelectedOptionCanvas.bbox("all"))

def get_items_by_category(category):
    items_dict = {
        "Programming Languages": programming_languages,
        "Frameworks and Libraries": frameworks_and_libraries,
        "Mobile Development": mobile_development,
        "Web Development": web_development,
        "UI/UX Design": ui_ux_design,
        "Game Development": game_development,
        "Software Engineering": software_engineering,
        "Cloud Computing": cloud_computing,
        "Security": security,
        "Data Science and Analytics": data_science_and_analytics,
        "Database Management": database_management,
        "Development Tools": development_tools,
        "Blockchain": blockchain,
        "Internet of Things (IoT)": Iot,
        "AI and Robotics": AI_and_Robotics,
        "Virtual Reality and Augmented Reality (VR/AR)": VR_AR,
        "Graphics Design": graphics_design,
        "User Interface": user_interface,
        "Project Management": project_management,
        "Business Skills": business_skills,
        "Regulatory and Compliance": regulatory_compliance,
        "Sustainability": sustainability,
        "Networking": networking,
        "Systems": systems,
        "Real Estate": realestate,
        "Communication": communication,
        "Management and Leadership": management_and_leadership,
        "Personal Development": personal_development,
        "Legal and Ethical": legal_and_ethical,
        "Technical Proficiency": Technical_proficiency,
        "Digital Collaboration": Digital_collaboration
    }
    return items_dict.get(category, [])

# Define available items
programming_languages = ["C#", "Java", "JavaScript", "Python", "PHP", "Kotlin", "Swift", "C++", "Bash", "R", "SQL"]
frameworks_and_libraries = ["NET", "Unity", "TensorFlow", "Keras", "React Native", "Xamarin", "Angular", "Node.js", "React", "Flask", "D3.js", "OpenCV"]
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
business_skills = ["Market Research", "Customer Behavior Analysis", "Market Analysis", "Strategic Planning", "Business Strategy", "Operational Efficiency", "Financial Planning", "Fundraising Strategies", "Competitive Intelligence", "Strategic Analysis", "Product Development", "Creativity"]
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
# Define other categories similarly

# Create category dropdown
categories = ["Programming Languages","Frameworks and libraries","Mobile Development","Web Development","UI/UX Design","Game Development","Software Engineering","Cloud Computing","Security","Data Science and Analytics","Database Management","Development Tools","Blockchain","IoT","AI and Robotics","VR/AR","Graphic Design","User Interface Design","Project Management","Business Skills","Regulatory and Compliance"," Sustainability","Networking","Systems","Real Estate","Communication","Management and Leadership","Personal Development","Legal and Ethical","Technical Proficiency","Digital Collaboration"]

window = tk.Tk()
window.geometry("700x450")
window.configure(bg="#173054")

canvas = tk.Canvas(
    window,
    bg="#173054",
    height=450,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(350.0, 225.0, image=image_image_1)

entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(472.5, 44.5, image=entry_image_1)

category_combobox = ttk.Combobox(canvas, values=categories)
category_combobox.place(x=357.0, y=29.0, width=231.0, height=29.0)
category_combobox.bind("<<ComboboxSelected>>", update_list)

canvas.create_text(
    47.0,
    85.0,
    anchor="nw",
    text="Available options:-",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 13 * -1)
)

canvas.create_text(
    392.0,
    84.0,
    anchor="nw",
    text="Selected options:-",
    fill="#FFFFFF",
    font=("LibreCaslonText Regular", 13 * -1)
)

canvas_frame = ttk.Frame(canvas, width=303.0, height=253.0)
canvas_frame.place(x=26.0, y=103.0)

SelectedOptionCanvas = tk.Canvas(canvas_frame, bg="#3A868F")
SelectedOptionCanvas.place(x=0, y=0, height=247, width=296)

vsb = tk.Scrollbar(SelectedOptionCanvas, orient="vertical", command=SelectedOptionCanvas.yview)
vsb.pack(side="right", fill="y")
SelectedOptionCanvas.config(yscrollcommand=vsb.set)
selected_listbox = tk.Listbox(canvas, width=48, height=15, selectmode=tk.MULTIPLE)
selected_listbox.place(x=377, y=106)
vsb_listbox = tk.Scrollbar(window, orient="vertical", command=selected_listbox.yview)
vsb_listbox.place(x=selected_listbox.winfo_x() + selected_listbox.winfo_width(), y=selected_listbox.winfo_y(), height=selected_listbox.winfo_height())
selected_listbox.config(yscrollcommand=vsb_listbox.set)


# Bind the events directly to the SelectedOptionCanvas
SelectedOptionCanvas.bind("<ButtonPress-1>", on_drag_start)
SelectedOptionCanvas.bind("<B1-Motion>", on_drag_motion)
SelectedOptionCanvas.bind("<ButtonRelease-1>", on_drag_end)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=287.0,
    y=385.0,
    width=126.0,
    height=36.0
)
window.resizable(True, True)
window.mainloop()
