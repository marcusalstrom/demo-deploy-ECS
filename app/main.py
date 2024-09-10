from flask import Flask, render_template
from itertools import cycle

app = Flask(__name__)


@app.route("/")
def canary_page():
    return render_template('canary.html', msg = "Spoon is the best Java source code analyser in the world!")

if __name__ == "__main__":
    app.run()
