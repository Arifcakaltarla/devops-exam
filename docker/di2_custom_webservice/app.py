from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/")
def root():
    return "Di2 custom webservice running\n"

if __name__ == "__main__":
    # DEVASC thread issue vermijden
    app.run(host="0.0.0.0", port=5000, threaded=False, use_reloader=False)
