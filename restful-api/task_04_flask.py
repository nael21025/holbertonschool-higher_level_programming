#!/usr/bin/python3
"""Task 4: Simple API using Flask Framework"""

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# In-memory users storage
users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint - welcomes user to the Flask API.
    
    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """
    Data endpoint - returns list of all usernames.
    
    Returns:
        list: List of all usernames (keys from users dict)
    """
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """
    Status endpoint - checks API status.
    
    Returns:
        str: "OK" if API is running
    """
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Get user endpoint - returns specific user data.
    
    Args:
        username (str): The username to retrieve
    
    Returns:
        dict: User data if found
        dict: Error message with 404 if not found
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add user endpoint - creates a new user.
    
    JSON body should contain:
        {
            "username": "unique_username",
            "name": "Full Name",
            "age": 25,
            "city": "City Name"
        }
    
    Returns:
        dict: Confirmation message with added user data (201)
        dict: Error message if:
            - Invalid JSON (400)
            - Username missing (400)
            - Username already exists (409)
    """
    # Try to parse JSON
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Check if data is None (empty or malformed JSON)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Check if username is provided
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data.get("username")
    
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Add the new user to users dictionary
    users[username] = data
    
    # Return 201 Created with confirmation message
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    # Run Flask with debug mode
    app.run(debug=True, host="127.0.0.1", port=5000)
