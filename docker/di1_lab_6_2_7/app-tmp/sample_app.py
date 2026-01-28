from flask import Flask, render_template
from werkzeug.serving import run_simple

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    run_simple("0.0.0.0", 8080, sample, threaded=False, use_reloader=False)
