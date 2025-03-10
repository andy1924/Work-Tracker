import tkinter as tk
from tkinter import messagebox
from work_tracker import WorkTracker

class WorkTrackerUI:
    def __init__(self, root, tracker):
        self.tracker = tracker
        root.title("Work Tracker")
        root.geometry("350x250")
        root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text=f"Welcome, {self.tracker.username}!", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        self.label.pack(pady=10)

        self.info_label = tk.Label(root, text="Track your work time and salary", font=("Arial", 10), bg="#f0f0f0", fg="#666")
        self.info_label.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Calculate Salary", command=self.show_salary, font=("Arial", 12),
                                          bg="#4CAF50", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3)
        self.calculate_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Timer", command=self.tracker.reset_timer, font=("Arial", 12),
                                      bg="#FF5733", fg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=3)
        self.reset_button.pack(pady=10)

        root.bind("<Motion>", self.tracker.mouse_moved)

    def show_salary(self):
        salary = self.tracker.calculate_salary()
        messagebox.showinfo("Salary Calculation", f"Total Salary: ₹{salary}")
