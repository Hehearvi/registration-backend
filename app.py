from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Registration backend running"})

@app.route('/register', methods=['POST'])
def register():

      if not request.is_json:
    return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    return jsonify({
        "message": "User registered successfully",
        "name": name,
        "email": email
    }), 201
