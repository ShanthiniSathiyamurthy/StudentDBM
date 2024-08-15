from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import font

def login():
    if e.get()=='' or e1.get()=='':
     messagebox.showerror('error','fields cannot be empty')
    elif e.get()=='shanthini' and  e1.get()=='ilan':
       messagebox.showinfo('sucess','welcome')
       window.destroy()
       import sms
    
    else:
       messagebox.showerror('error','please enter vaild name or password')

# Create the main application window
window = tk.Tk()
window.title("Welcome")
window.geometry('400x400')  # Set the window size
window.resizable(False, False)  # Disable resizing

# Define fonts and colors for styling
title_font = font.Font(family="Helvetica", size=15, weight="bold")
label_font = font.Font(family="Arial", size=12)
entry_font = font.Font(family="Arial", size=12)

# Create and style the greeting label
greeting = tk.Label(window, text="Student Login Form", font=title_font, fg="darkblue")
greeting.place(x=100, y=10)

# Create and style the "Name" label
l = tk.Label(window, text="Name", font=label_font, fg="black")
l.place(x=50, y=70)

# Create and style the "Name" entry field
e = tk.Entry(window, font=entry_font, borderwidth=2, relief="groove")
e.place(x=140, y=70)

# Create and style the "Password" label
l1 = tk.Label(window, text="Password", font=label_font, fg="black")
l1.place(x=50, y=120)

# Create and style the "Password" entry field
e1 = tk.Entry(window, font=entry_font, show="*", borderwidth=2, relief="groove")
e1.place(x=140, y=120)

# Create and style the "Login" button
b = tk.Button(window, text="Login", font=label_font, command=login, bg="lightblue", fg="black", padx=10, pady=5, borderwidth=2, relief="raised")
b.place(x=150, y=170)

# Run the Tkinter event loop
window.mainloop()
