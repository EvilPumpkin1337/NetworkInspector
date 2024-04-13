import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from logic import *
from settings import *
from core import *
import menu

def test():
    print("test")

# Create the main window

window = tk.Tk()
window.title("NetworkInspector")
window.geometry("480x350")
window.configure(bg="#06061c")
window.wm_iconphoto(True, ImageTk.PhotoImage(Image.open("logo.ico")))


# Create Buttons

back_button = tk.Button( window, text="Back", bg="#2b2b2b", fg="white", command=test, width=10 )
back_button.grid(ipadx=1, ipady=1, row=0, column=0, columnspan=1)

start_button= tk.Button( window, text="Start", bg="#00ff0d", fg="#000000", command=test )
start_button.grid(ipadx=1, ipady=1, row=0, column=1, columnspan=1)

stop_button= tk.Button( window, text="Stop", bg="#ff0000", fg="#000000", command=test)
stop_button.grid(ipadx=1, ipady=1, row=0, column=2, columnspan=1)


# Create tables

columns =[
    "Time","Source IP Address", "MAC Address","Destination IP Address", "Port"
]

data = [
    ("14:00", "192.168.1.9", "00:11:22:33:44:99", "192.168.1.10", 24),
    ("15:00", "192.168.1.11", "00:11:22:33:44:00", "192.168.1.12", 25),
    ("16:00", "192.168.1.13", "00:11:22:33:44:11", "192.168.1.14", 26),
    ("17:00", "192.168.1.15", "00:11:22:33:44:22", "192.168.1.16", 143),
    ("18:00", "192.168.1.17", "00:11:22:33:44:33", "192.168.1.18", 28),
    ("19:00", "192.168.1.19", "00:11:22:33:44:44", "192.168.1.20", 25),
    ("20:00", "192.168.1.21", "00:11:22:33:44:55", "192.168.1.22", 30),
]


IPtable = ttk.Treeview(window, columns=columns, show="headings", 
                    style="Treeview", height=20, selectmode="browse")

for item in data:
    IPtable.insert("", "end", values=item)



style = ttk.Style()
style.configure("Treeview", background="#00092b", foreground="white", fieldbackground="#00092b", bordercolor="#00092b")


IPtable.heading("Time", text="Time")
IPtable.heading("Source IP Address", text="Source IP Address")
IPtable.heading("MAC Address", text="MAC Address")
IPtable.heading("Destination IP Address", text="Destination IP Address")
IPtable.heading("Port", text="Port")


IPtable.column("Time",minwidth=1, width=1)
IPtable.column("Port", minwidth=1, width=1)
IPtable.grid( padx=1, pady=70, row=1, column=0, sticky="nsew" )



DATAtable = ttk.Treeview(window)
DATAtable.heading('#0', text="Packet Data", anchor=tk.W)
DATAtable.column('#0',minwidth=1, width=1)
DATAtable.grid( ipadx=350, ipady=80, row=2, column=0, columnspan=3)







window.columnconfigure(0, weight=1)
window.mainloop()


