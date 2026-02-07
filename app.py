from flask import Flask, request, jsonify

# Create Flask application
app = Flask(__name__)

# Home route to check if backend is running
@app.route('/')
def home():
    return jsonify({"message": "Registration backend running"})

# Registration API endpoint
@app.route('/register', methods=['POST'])
def register():

    # Check if request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get JSON data from request
    data = request.get_json()

    # Extract user details from request
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # Validate required fields
    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Send success response if validation passes
    return jsonify({
        "message": "User registered successfully",
        "name": name,
        "email": email
    }), 201
