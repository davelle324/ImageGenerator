# app.py

from flask import Flask, redirect, render_template, request, session, url_for
import secrets
from prompt import generate_response
app = Flask(__name__)
# Create a session key so that info is saved through sessions
app.secret_key = secrets.token_hex()

# placeholder text for prompt
PLACEHOLDER_CODE = "What can I ask you"

@app.route("/", methods=["GET"])
def prompt():
    # set placeholder text if textbox is empty
    if session.get("prompt") is None:
        session["prompt"] = PLACEHOLDER_CODE
    if session.get("response") is None:
        session["response"] = ""
    context = {
        "prompt": session["prompt"],
        "response": session["response"]
    }
    return render_template("code_input.html", **context)

@app.route("/submit_request", methods=["POST"])
def submit_request():
    session["prompt"] = request.form.get("prompt")
    session["response"] = generate_response(session["prompt"])
    return redirect(url_for("prompt"))

@app.route("/reset_session", methods=["POST"])
def reset_session():
    session.clear()
    session["prompt"] = ""
    session["response"] = ""
    return redirect(url_for("prompt"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
