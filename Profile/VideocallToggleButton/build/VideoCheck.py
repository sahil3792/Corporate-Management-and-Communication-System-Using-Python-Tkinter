import tkinter as tk
from vidstream import CameraClient

def toggle_camera():
    global camera_enabled
    camera_enabled = not camera_enabled

def update_video():
    global camera_enabled
    if camera_enabled:
        frame = camera_client.read()
        video_label.img = tk.PhotoImage(data=frame)
        video_label.config(image=video_label.img)
    else:
        video_label.config(image="")
    window.after(10, update_video)

def main():
    global window, video_label, camera_client, camera_enabled
    window = tk.Tk()
    window.title("Camera Feed")
    
    camera_enabled = False
    
    toggle_button = tk.Button(window, text="Toggle Camera", command=toggle_camera)
    toggle_button.pack(pady=10)
    
    video_label = tk.Label(window)
    video_label.pack()
    
    camera_client = CameraClient('192.168.1.109', 9999)  # Replace with the server IP address and port
    camera_client.start_stream()

    update_video()

    window.mainloop()

if __name__ == "__main__":
    main()
