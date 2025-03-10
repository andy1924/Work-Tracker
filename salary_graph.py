import matplotlib.pyplot as plt


class SalaryGraph:
    def __init__(self, username):
        self.username = username
        self.time_worked = []
        self.salaries = []

    def update_graph(self, total_time, salary):
        """Updates the graph with time in seconds instead of hours."""
        time_worked_seconds = max(round(total_time * 3600, 2), 1)  # Convert hours to seconds, ensuring no 0 values

        self.time_worked.append(time_worked_seconds)
        self.salaries.append(salary)

        plt.figure(figsize=(6, 4))
        plt.plot(self.time_worked, self.salaries, marker='o', linestyle='-', color='b', label="Salary Earned")
        plt.xlabel("Time Worked (Seconds)")
        plt.ylabel("Salary (₹)")
        plt.title(f"Salary Progress - {self.username}")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()

        # Show updated graph
        plt.show()
