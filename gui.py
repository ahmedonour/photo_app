import tkinter as tk
import threading
import webbrowser
import socket
import os
from app import app  # Import Flask app from your app.py
from pathlib import Path
# import qrcode
from PIL import Image, ImageTk


def run_server():
    app.run(host='0.0.0.0', port=2000, debug=False, use_reloader=False)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return 'localhost'

def launch_gui():
    ip = get_local_ip()
    url = f"http://{ip}:2000"

    # Start Flask server in a thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

   

    # GUI window
    root = tk.Tk()
    root.title("📷 2:2 Photo Capture App")
    root.geometry("400x600")
    root.configure(bg="#000")

    lbl = tk.Label(root, text="Access the Web App at:", font=("Arial", 12), fg="white", bg="#000")
    lbl.pack(pady=10)

    ip_label = tk.Label(root, text=url, font=("Courier", 14, "bold"), fg="#00ffcc", bg="#000")
    ip_label.pack(pady=10)

    # def open_browser():
    #     webbrowser.open(url)

    # btn_open = tk.Button(root, text="🌐 Open in Browser", command=open_browser, bg="#1e90ff", fg="white", font=("Arial", 12), relief="raised", bd=2)
    # btn_open.pack(pady=10)

# Show actual network IP for connecting from other devices
     
    port = 2000
    network_url = f"http://{ip}:{port}"


# Open localhost for the local desktop GUI
    # def open_localhost_browser():
    #     webbrowser.open("http://localhost:5000")
    def open_localhost_browser():
        webbrowser.open(f"http://localhost:{port}")


# Show network IP in the label
    # ip_label = tk.Label(root, text=network_url, font=("Courier", 14, "bold"), fg="#00ffcc", bg="#000")
    # ip_label.pack(pady=10)

    btn_open = tk.Button(root, text="🌐 Open in Browser (Localhost)", command=open_localhost_browser, bg="#1e90ff", fg="white", font=("Arial", 12), relief="raised", bd=2)
    btn_open.pack(pady=10)


    # Create Customer-Photo folder on Desktop
    save_path = Path.home() / "Desktop" / "Customer-Photo"
    save_label = tk.Label(root, text=f"Photos saved to:\n{save_path}", fg="#0f0", bg="#000", font=("Arial", 9))
    save_label.pack(pady=10)

    note = tk.Label(root, text="Make sure your other device is\non the same Wi-Fi network.", fg="#aaa", bg="#000", font=("Arial", 10))
    note.pack(pady=10)
    # Generate QR code for network URL
    # qr_img = qrcode.make(url)
    # qr_path = "qr_temp.png"
    # qr_img.save(qr_path)
    
    # # Load QR code image into Tkinter
    # qr_pil = Image.open(qr_path)
    # qr_pil = qr_pil.resize((150, 150), Image.Resampling.LANCZOS)
    # qr_tk = ImageTk.PhotoImage(qr_pil)
    
    # qr_label = tk.Label(root, image=qr_tk, bg="#000")
    # qr_label.image = qr_tk  # Keep reference
    # qr_label.pack(pady=5)
    
    # tk.Label(root, text="Scan with phone to open", fg="#ccc", bg="#000", font=("Arial", 9)).pack()


    root.mainloop()

if __name__ == '__main__':
    launch_gui()
