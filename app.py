from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def krijg_beschrijvingen():
    kenmerken1 = request.form.get('kenmerken1', '')

    return render_template("ziektegenen.html",
                           kenmerken1=kenmerken1)


if __name__ == '__main__':
    app.run()