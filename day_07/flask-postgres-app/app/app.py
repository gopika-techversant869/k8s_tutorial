from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

DATA_FILE = "data.json"

# Load data from file if exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
else:
    users = []

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    user_id = len(users) + 1
    users.append({"id": user_id, "name": name})
    save_data()
    return jsonify({"message": f"User {name} added successfully."}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
