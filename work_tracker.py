import time
import tkinter as tk
from tkinter import messagebox
import threading
import os
import json
from idle_tracker import IdleTracker
from salary_graph import SalaryGraph


class WorkTracker:
    def __init__(self, username, root):
        self.username = username
        self.start_time = time.time()
        self.idle_time = 0
        self.last_active = time.time()
        self.data_file = f"{username}_work_data.json"
        self.salary_per_hour = self.get_salary_from_db(username)
        self.overtime_bonus = 1.5
        self.load_data()

        self.root = root
        self.create_ui()
        self.idle_tracker = IdleTracker(self)
        self.salary_graph = SalaryGraph(self.username)  # Graph Instance
        threading.Thread(target=self.idle_tracker.track_idle_time, daemon=True).start()

    def get_salary_from_db(self, username):
        """Fetches salary from user database."""
        with open("users.json", "r") as f:
            users = json.load(f)
        return users.get(username, {}).get("hourly_salary", 100)  # Default ₹100/hr

    def load_data(self):
        """Loads saved work data from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.start_time = data.get("start_time", self.start_time)
                self.idle_time = data.get("idle_time", 0)

    def save_data(self):
        """Saves work data to a JSON file."""
        with open(self.data_file, "w") as f:
            json.dump({"start_time": self.start_time, "idle_time": self.idle_time}, f)

    def calculate_salary(self):
        """Calculates salary with overtime and idle deductions."""
        total_time = (time.time() - self.start_time) / 3600
        active_time = total_time - (self.idle_time / 3600)
        overtime = max(0, active_time - 8)
        salary = (active_time * self.salary_per_hour) + (overtime * self.salary_per_hour * self.overtime_bonus)
        return round(salary, 2), round(active_time, 2)

    def reset_timer(self):
        """Resets the timer only after 1 month."""
        current_time = time.time()
        elapsed_days = (current_time - self.start_time) / (24 * 3600)

        if elapsed_days >= 30:
            self.start_time = current_time
            self.idle_time = 0
            self.save_data()
            messagebox.showinfo("Reset", "Timer reset for a new month!")
        else:
            messagebox.showwarning("Reset Blocked", "Timer resets only after 1 month!")

    def mouse_moved(self, event):
        """Resets last active time when the user moves the mouse."""
        self.last_active = time.time()

    def create_ui(self):
        """Creates the UI for Work Tracker."""
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        tk.Label(self.root, text=f"Work Tracker - Welcome {self.username}", font=("Arial", 16, "bold"),
                 bg="#f0f0f0", fg="#333").pack(pady=10)

        tk.Button(self.root, text="Calculate Salary", command=self.show_salary, font=("Arial", 12),
                  bg="#4CAF50", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3).pack(pady=10)

        tk.Button(self.root, text="Reset Timer", command=self.reset_timer, font=("Arial", 12),
                  bg="#FF5733", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3).pack(pady=10)

        self.root.bind("<Motion>", self.mouse_moved)

    def show_salary(self):
        """Displays calculated salary in a message box and updates graph."""
        salary, time_worked = self.calculate_salary()
        self.salary_graph.update_graph(time_worked, salary)
        messagebox.showinfo("Salary Calculation", f"Total Salary: ₹{salary}")
