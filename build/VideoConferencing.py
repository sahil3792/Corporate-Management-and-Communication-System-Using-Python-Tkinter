def VideoConferencing():
    frame = Frame(window, bg="#ECECD9", bd=0, height=450, width=510)
    frame.place(x=36, y=0)

    server = StreamingServer(socket.gethostbyname(socket.gethostname()), 9999)
    receiver = AudioReceiver(socket.gethostbyname(socket.gethostname()), 8888)

    def start_listening():
        threading.Thread(target=server.start_server).start()
        threading.Thread(target=receiver.start_server).start()

    def start_camera_stream(target_ips):
        for target_ip in target_ips:
            camera_client = CameraClient(target_ip, 7777)
            threading.Thread(target=camera_client.start_stream).start()

    def start_screen_sharing(target_ips):
        for target_ip in target_ips:
            screen_client = ScreenShareClient(target_ip, 7777)
            threading.Thread(target=screen_client.start_stream).start()

    def start_audio_stream(target_ips):
        for target_ip in target_ips:
            audio_sender = AudioSender(target_ip, 6666)
            threading.Thread(target=audio_sender.start_stream).start()

    def start_streams():
        target_ips = text_target_ip.get(1.0, 'end-1c').strip().split()
        start_camera_stream(target_ips)
        start_screen_sharing(target_ips)
        start_audio_stream(target_ips)

    label_target_ip = tk.Label(frame, text="Enter target IPs separated by space:")
    label_target_ip.pack()

    text_target_ip = tk.Text(frame, height=1)
    text_target_ip.pack()

    btn_listen = tk.Button(frame, text="Start Listening", width=50, command=start_listening)
    btn_listen.pack(anchor=tk.CENTER, expand=True)

    btn_start_streams = tk.Button(frame, text="Start Streams", width=50, command=start_streams)
    btn_start_streams.pack(anchor=tk.CENTER, expand=True)

    window.after(1000, start_streams)
