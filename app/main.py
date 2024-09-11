from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def canary_page():
    return render_template('canary_v1.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
