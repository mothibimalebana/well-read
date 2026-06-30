from flask import Flask

app = Flask(__name__)

# connect to database

if __name__ == "__main__":
    app.run(debug=True)