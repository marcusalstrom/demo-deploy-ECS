from flask import Flask, render_template
from itertools import cycle

app = Flask(__name__)

messages = cycle([
    "DevOps is where its at yo!",
    "I eat bugs for breakfast",
    "I much prefer this to my old job",
    "Spoon is NOT the best Java source code analyser in the world!"
])
@app.route("/")
def canary_page():
    return render_template('canary.html', msg = next(messages))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
