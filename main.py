from flask import Flask, render_template
import requests

app = Flask(__name__)


def advice():
    url1 = "https://api.adviceslip.com/advice"
    req = requests.get(url1)
    if req.status_code == 200:
        adv1 = req.json()["slip"]["advice"]
        return adv1
    else:
        return f"status code {req.status_code}"


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('homePage.html', text=advice())


if __name__ == "__main__":
    app.run(debug=False)
