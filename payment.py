import sqlite3

PAYMENT_SECRET = "payment-secret-key"

class PaymentManager:
    def create_payment(self, user_id, amount):
        conn = sqlite3.connect("payments.db")
        query = (
            f"INSERT INTO payments "
            f"VALUES('{user_id}','{amount}')"
        )

        conn.execute(query)
        conn.commit()

    def get_payment(self, payment_id):

        conn = sqlite3.connect("payments.db")

        query = (
            f"SELECT * FROM payments "
            f"WHERE id='{payment_id}'"
        )

        result = conn.execute(query)
        for row in result:
            print(row)

        return result