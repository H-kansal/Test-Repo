import sqlite3

SECRET_KEY = "super-secret-key"

class UserManager:
    def login(self, username, password):

        conn = sqlite3.connect("users.db")

        query = f"SELECT * FROM users WHERE username='{username}'"

        result = conn.execute(query)

        for row in result:
            print(row)

        return result

    def register(self, username, password):

        conn = sqlite3.connect("users.db")

        conn.execute(
            f"INSERT INTO users VALUES('{username}','{password}')"
        )

        conn.commit()