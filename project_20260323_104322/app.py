import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
      <head>
        <title>Simple Flask App</title>
      </head>
      <body>
        <h1>Welcome to the Simple Flask App</h1>
        <button style="background-color: yellow;">Click Me</button>
      </body>
    </html>
    """

port = int(os.environ.get("PORT", 5001))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)