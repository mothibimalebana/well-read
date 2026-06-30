from flask import Flask
import psycopg

app = Flask(__name__)

# connect to database
with psycopg.connect("postgresql://myuser:mypassword@localhost:5432/mydatabase") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            select * from test;
            """)
        print(cur.fetchone())

if __name__ == "__main__":
    app.run(debug=True)