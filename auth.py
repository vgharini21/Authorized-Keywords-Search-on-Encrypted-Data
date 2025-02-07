from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

users = {"user1": "password1", "user2": "password2"}  # Replace with a database

def authenticate(username, password):
    if users.get(username) == password:
        return create_access_token(identity=username)
    return None

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    token = authenticate(data["username"], data["password"])
    return jsonify(access_token=token) if token else jsonify({"error": "Invalid credentials"}), 401
