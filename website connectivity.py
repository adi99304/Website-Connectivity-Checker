import tkinter as tk
import socket
import ssl

def check_website():
    url = entry_url.get()
    try:
        # Attempt HTTP connection
        connection = socket.create_connection((url, 80), timeout=5)
        connection.close()
        result_label.config(text="Website is Accessible", fg='green')
        return
    except (socket.gaierror, socket.timeout, ConnectionRefusedError) as e:
        print("HTTP Error:", e)

    try:
        # Attempt HTTPS connection
        context = ssl.create_default_context()
        with socket.create_connection((url, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                result_label.config(text="Website is Accessible", fg='green')
    except Exception as e:
        print("HTTPS Error:", e)
        result_label.config(text="Website is Not Accessible", fg='red')

root = tk.Tk()
root.geometry("800x220")
root.title("Website Connectivity Checker")
root.config(bg='#F0F0F0')

header_label = tk.Label(root, text="Website Connectivity Checker", font=('Arial bold', 18), bg='#6E7B8B', fg='white')
header_label.pack(pady=10)

url_frame = tk.Frame(root, bg='#F0F0F0')
url_frame.pack(pady=10)

url_label = tk.Label(url_frame, text="Enter Website URL:", font=('Arial', 12), bg='#F0F0F0')
url_label.grid(row=0, column=0, padx=(20, 10))

entry_url = tk.Entry(url_frame, font=('Arial', 12), justify=tk.CENTER, relief=tk.SOLID, width=30)
entry_url.grid(row=0, column=1, padx=(0, 20))

check_button = tk.Button(root, text="Check", font=('Arial bold', 12), bg='#6E7B8B', fg='white', bd=3, padx=10, command=check_website)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial bold', 14), bg='#F0F0F0')
result_label.pack()

root.mainloop()
