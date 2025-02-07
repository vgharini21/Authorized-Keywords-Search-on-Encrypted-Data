from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from search import search_keyword
from access_control import grant_access

app = Flask(__name__)

@app.route("/grant-access", methods=["POST"])
@jwt_required()
def grant():
    user = get_jwt_identity()
    data = request.json
    keyword = data["keyword"]
    if grant_access(user, keyword, 60):
        return jsonify({"message": "Access granted."})
    return jsonify({"error": "Unauthorized"}), 403

@app.route("/search", methods=["POST"])
@jwt_required()
def search():
    user = get_jwt_identity()
    data = request.json
    keyword = data["keyword"]
    return jsonify({"result": search_keyword(user, keyword)})

if __name__ == "__main__":
    app.run(debug=True)
