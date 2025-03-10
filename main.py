import tkinter as tk
from tkinter import messagebox
from auth import Auth
from work_tracker import WorkTracker


def login_screen():
    """Creates the login/register UI."""
    def login():
        username = entry_username.get()
        password = entry_password.get()
        if auth.login(username, password):
            root.destroy()  # Close login window
            open_work_tracker(username)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def register():
        username = entry_username.get()
        password = entry_password.get()
        salary = entry_salary.get()

        if not salary.isdigit():
            messagebox.showerror("Error", "Salary must be a number!")
            return

        success, msg = auth.register(username, password, float(salary))
        messagebox.showinfo("Info", msg)

    auth = Auth()
    root = tk.Tk()
    root.title("Login/Register")
    root.geometry("300x250")

    tk.Label(root, text="Username:").pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password:").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Label(root, text="Hourly Salary (Only for Registration):").pack()
    entry_salary = tk.Entry(root)
    entry_salary.pack()

    tk.Button(root, text="Register", command=register).pack(pady=5)
    tk.Button(root, text="Login", command=login).pack(pady=5)

    root.mainloop()


def open_work_tracker(username):
    """Opens the work tracker UI properly."""
    root = tk.Tk()
    root.title(f"Work Tracker - Welcome {username}")
    WorkTracker(username, root)  # Initialize WorkTracker with username
    root.mainloop()


if __name__ == "__main__":
    login_screen()
