import tkinter as tk
from tkinter import messagebox

#Create the function for the username and password
def login():
  username = username_entry.get()
  password = password_entry.get()
  
  if username == "ElCapitan123+" and password == "Qwerty123+":
    messagebox.showinfo("Login", "Login Successful!")
    window.destroy()
  else:
    messagebox.showerror("Login", "Incorrect username or password")

#Customize the window's appearance
window = tk.Tk()
window.title("Authorization")
window.geometry("300x150")

#Apply the username to the window
tk.Label(window, text="Username").pack()
username_entry = tk.Entry(window)
username_entry.pack()

#Apply the password to the password
tk.Label(window, text="Password").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

#Give the user and alternate way to give username and password
def handle_enter(event):
  login()

window.bind("<Return>", handle_enter)

#Apply the button and customize
tk.Button(window, text="Login", command=login).pack()

window.mainloop()

