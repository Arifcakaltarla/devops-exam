from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    return jsonify({
        "message": "login received",
        "username": username
    })

@app.route("/api/feedback", methods=["POST"])
def feedback():
    name = request.form.get("name")
    message = request.form.get("message")

    return jsonify({
        "from": name,
        "message": message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
