from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>IP Test</h1>
    <p>Това е доброволна демонстрация. Сайтът не записва IP адреси.</p>
    <p>Посетителите не биват проследявани.</p>
    """
