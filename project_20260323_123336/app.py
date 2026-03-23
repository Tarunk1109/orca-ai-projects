import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Flask App</title>
        <style>
            button {
                background-color: violet;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Simple Flask App</h1>
        <button>Click me</button>
        <p>Timestamp: 2026-03-23 12:33:36</p>
    </body>
    </html>
    """

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)