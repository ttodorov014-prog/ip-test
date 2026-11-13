
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        consent = request.form.get("consent")

        if consent == "yes":
            ip = request.headers.get(
                "X-Forwarded-For",
                request.remote_addr
            ).split(",")[0].strip()

            print("CONSENTED IP:", ip, flush=True)
            message = "IP адресът беше изпратен успешно!"

    return f"""
    <h1>IP Test</h1>

    <p>
    Ако натиснеш бутона, твоят IP адрес ще бъде
    изпратен на собственика на сайта.
    </p>

    <form method="POST">
        <button name="consent" value="yes" type="submit">
            Съгласен съм – изпрати IP
        </button>
    </form>

    <p>{message}</p>
    """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>IP Test</h1>
    <p>Това е доброволна демонстрация. Сайтът не записва IP адреси.</p>
    <p>Посетителите не биват проследявани.</p>
    """
