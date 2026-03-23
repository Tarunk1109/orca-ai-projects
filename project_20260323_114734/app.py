import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <style>
                button {
                    background-color: green;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    cursor: pointer;
                    font-size: 16px;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Green Button App</h1>
            <button>Click Me</button>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)