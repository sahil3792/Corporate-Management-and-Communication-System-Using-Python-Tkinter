import cv2
from PIL import Image, ImageTk
import tkinter as tk

def toggle_camera():
    global camera_on, cap, camera_label
    if camera_on:
        # Turn off camera
        cap.release()  # Release the camera
        camera_label.config(image=None)  # Clear the label
        print("Camera turned off")
        camera_on = False
    else:
        # Turn on camera
        cap = cv2.VideoCapture(0)  # Open default camera (index 0)
        if cap.isOpened():
            camera_on = True
            update_camera_feed()  # Start updating camera feed
            print("Camera turned on")
        else:
            print("Error: Could not open camera")

def update_camera_feed():
    ret, frame = cap.read()  # Read a frame from the camera
    if ret:
        # Convert the frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Resize the frame to your desired size
        frame = cv2.resize(frame, (640, 480))
        # Convert the frame to a format compatible with Tkinter
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        # Update the label with the new frame
        camera_label.imgtk = imgtk
        camera_label.config(image=imgtk)
        # Schedule the next update after 10 ms
        window.after(10, update_camera_feed)
    else:
        print("Error: Failed to capture frame")

# GUI setup
window = tk.Tk()
window.title("Camera Feed")
window.geometry("640x520")

camera_on = False  # Initial state of camera
cap = None  # Capture object for camera
camera_label = tk.Label(window)
camera_label.pack()

toggle_button = tk.Button(window, text="Toggle Camera", command=toggle_camera)
toggle_button.pack()

window.mainloop()
