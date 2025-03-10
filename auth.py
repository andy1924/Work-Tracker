import json
import os
import hashlib


class Auth:
    def __init__(self):
        self.user_data_file = "users.json"
        if not os.path.exists(self.user_data_file):
            with open(self.user_data_file, "w") as f:
                json.dump({}, f)

    def hash_password(self, password):
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password, salary_per_hour):
        """Registers a new user with a hashed password."""
        with open(self.user_data_file, "r") as f:
            users = json.load(f)

        if username in users:
            return False, "User already exists!"

        users[username] = {
            "password": self.hash_password(password),
            "hourly_salary": salary_per_hour
        }

        with open(self.user_data_file, "w") as f:
            json.dump(users, f)

        return True, "Registration successful!"

    def login(self, username, password):
        """Validates username and password during login."""
        with open(self.user_data_file, "r") as f:
            users = json.load(f)

        if username in users and users[username]["password"] == self.hash_password(password):
            return True
        return False
