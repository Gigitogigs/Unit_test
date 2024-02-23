import tkinter as tk
from unittest import TestCase, main
from tkinter import messagebox

def login(username, password):
    # Replace this with your actual login logic
    return username == "admin" and password =="admin"

def on_login_button_clicked():
    username = entry_username.get()
    password = entry_password.get()
    if login(username, password):
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create a tkinter window
window = tk.Tk()
window.title("Login")

# Username label and entry
label_username = tk.Label(window, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
label_password = tk.Label(window, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Login button
btn_login = tk.Button(window, text="Login", command=on_login_button_clicked)
btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the tkinter event loop
window.mainloop()

class TestLogin(TestCase):
    def test_login_with_valid_credentials(self):
        result = login("test_user", "test_password")
        self.assertTrue(result)

    def test_login_with_no_username(self):
        result = login("", "test_password")
        self.assertFalse(result)

    def test_login_with_no_password(self):
        result = login("test_user", "")
        self.assertFalse(result)

if __name__ == "__main__":
    main()