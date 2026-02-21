
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET = "dev-secret-key"

users = {
    "admin": "password123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        token = jwt.encode({
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET, algorithm="HS256")

        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/protected")
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token missing"}), 403

    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        return jsonify({"message": f"Welcome {decoded['user']}"})
    except:
        return jsonify({"error": "Invalid token"}), 403

if __name__ == "__main__":
    app.run(port=5000)
