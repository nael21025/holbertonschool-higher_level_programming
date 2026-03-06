#!/usr/bin/python3
"""Task 5: API Security and Authentication using Flask-HTTPAuth and Flask-JWT-Extended"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Configure JWT
app.config["JWT_SECRET_KEY"] = "your-secret-key-change-in-production"

# Initialize authentication
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user storage with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ============================================================================
# BASIC AUTHENTICATION HANDLERS
# ============================================================================

@auth.verify_password
def verify_password(username, password):
    """
    Verify basic authentication credentials.
    
    Args:
        username (str): Username from Basic Auth header
        password (str): Password from Basic Auth header
    
    Returns:
        str: Username if credentials are valid, None otherwise
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Authentication.
    
    Requires HTTP Basic Authentication credentials.
    
    Returns:
        str: Success message if authenticated
    """
    return "Basic Auth: Access Granted"


# ============================================================================
# JWT AUTHENTICATION HANDLERS
# ============================================================================

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle malformed or invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle when fresh token is required"""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint - returns JWT token upon successful authentication.
    
    Expected JSON body:
        {
            "username": "user1",
            "password": "password"
        }
    
    Returns:
        dict: JWT access token (201)
        dict: Error message if credentials invalid (401)
        dict: Error message if invalid JSON (400)
    """
    # Parse JSON request
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    # Verify credentials
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 401
    
    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Create JWT token with user info
    access_token = create_access_token(identity=username)
    
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.
    
    Requires valid JWT token in Authorization header:
        Authorization: Bearer <token>
    
    Returns:
        str: Success message if authenticated
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only protected route using JWT with role-based access.
    
    Requires:
        - Valid JWT token in Authorization header
        - Token must belong to a user with 'admin' role
    
    Returns:
        str: Success message if user is admin
        dict: Error message if not admin (403)
    """
    current_user = get_jwt_identity()
    
    # Check if user has admin role
    if users[current_user].get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


# ============================================================================
# STATUS AND UTILITY ENDPOINTS
# ============================================================================

@app.route("/", methods=["GET"])
def home():
    """
    Home endpoint - provides API information.
    
    Returns:
        dict: API status and available endpoints
    """
    return jsonify({
        "message": "Welcome to Secure API",
        "version": "1.0",
        "endpoints": {
            "authentication": {
                "basic": "GET /basic-protected (requires Basic Auth)",
                "jwt_login": "POST /login (returns JWT token)",
                "jwt_protected": "GET /jwt-protected (requires JWT)",
                "admin_only": "GET /admin-only (requires admin JWT)"
            }
        },
        "test_credentials": {
            "user": "user1 / password",
            "admin": "admin1 / password"
        }
    })


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
