from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <html>
        <head>
            <style>
                button {
                    background-color: yellow;
                    border: none;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Simple Flask App</h1>
            <button>Click Me</button>
        </body>
    </html>
    '''

port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)