from flask import Flask, session, redirect, url_for, request,template, render_template_string

app = Flask(__name__)
app.secret_key = "segredo_super_secreto"  

@app.route("/contador", methods=["GET", "POST"])
def contador():
    if "contador" not in session:
        session["contador"] = 0

    if request.method == "POST" and request.form.get("acao") == "zerar":
        session["contador"] = 0
    else:
        session["contador"] += 1

    return render_template_string(template, contador=session["contador"])


if __name__ == "__main__":
    app.run(debug=True)
