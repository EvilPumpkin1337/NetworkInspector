import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from logic import *
from settings import *
from core import *
#import menu

def test():
    print("test")
def test2():
    print("test2")

def test3():
    print("test3")

def search():
    query = search_entry.get().lower()  # Get the search query from the entry widget

    for item in IPtable.get_children():  # Loop through each item in the Treeview
        values = IPtable.item(item, 'values')

        if query in map(str.lower, values):  # Check if the query matches any value in the item
            IPtable.selection_set(item)  # Select the item if it matches the query

        else:
            IPtable.selection_remove(item)  # Deselect the item if it doesn't match the query



def on_entry_click(event):
    if entry.get() == "Search":
        entry.delete(0, tk.END)
        entry.configure(foreground='black')

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Search")
        entry.configure(foreground='gray')


# Create the main window ==============================================================================================================
window = tk.Tk()
window.title("NetworkInspector")
window.geometry("480x350" )
window.configure(bg="#06061c")
window.wm_iconphoto(True, ImageTk.PhotoImage(Image.open("logo.ico")))

# Create Buttons ==============================================================================================================


back_button = ttk.Button(window, text="Back", command=test)
back_button.place(x=10, y=10)

start_button  = ttk.Button(window, text="Start", command=test2)
start_button.place(x=250, y=10)

stop_button  = ttk.Button(window, text="Stop", command=test3)
stop_button.place(x=350 , y=10)

save_button  = ttk.Button(window, text="Save", command=test3)
save_button.place(x=450, y=10)

load_button  = ttk.Button(window, text="Load", command=test3)
load_button.place(x=550, y=10)

filter_button  = ttk.Button(window, text="Filter", command=test3)
filter_button.place(x=1230, y=55)


style = ttk.Style()
style.configure('Transparent.TEntry', foreground='#1c1c1c')  # Set default text color

search_entry = ttk.Entry(window, width=150 , style='Transparent.TEntry')
search_entry.place(x=10, y=60)

search_entry.insert(0, "Search")
search_entry.bind("<FocusIn>", on_entry_click)
search_entry.bind("<FocusOut>", on_focus_out)

# Create tables ==============================================================================================================

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
                    style="Treeview", selectmode="browse")

for item in data:
    IPtable.insert("", "end", values=item)



style = ttk.Style()
style.configure("Treeview", background="#00092b", foreground="white", fieldbackground="#00092b", bordercolor="#00092b")


IPtable.heading("Time", text="Time")
IPtable.heading("Source IP Address", text="Source IP Address")
IPtable.heading("MAC Address", text="MAC Address")
IPtable.heading("Destination IP Address", text="Destination IP Address")
IPtable.heading("Port", text="Port")


IPtable.column("Time",minwidth=1, width=100)
IPtable.column("Source IP Address", minwidth=1, width=270)
IPtable.column("MAC Address",minwidth=1, width=270)
IPtable.column("Destination IP Address", minwidth=1, width=300)
IPtable.column("Port",minwidth=1, width=100)
IPtable.place(x=10, y=100, height=300, width=1340)


DATAtable = ttk.Treeview(window, height=12, selectmode="browse")
DATAtable.heading('#0', text="Packet Data", )
DATAtable.column('#0',minwidth=1, width=1340)
DATAtable.place(x=10, y=420)


window.rowconfigure(0, weight=1)  # IPtable
window.rowconfigure(1, weight=1)  # DATAtable

window.columnconfigure(0, weight=1)
window.mainloop()


