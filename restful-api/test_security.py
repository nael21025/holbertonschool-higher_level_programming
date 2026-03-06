#!/usr/bin/python3
"""Test script for Security API - task_05_basic_security.py"""

import requests
import json
import base64

BASE_URL = "http://127.0.0.1:5000"


def test_basic_auth():
    """Test Basic Authentication"""
    print("="*60)
    print("TESTING BASIC AUTHENTICATION")
    print("="*60 + "\n")
    
    # Without credentials
    print("1. Without credentials:")
    response = requests.get(f"{BASE_URL}/basic-protected")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json() if response.status_code != 200 else response.text}\n")
    
    # With valid credentials
    print("2. With valid credentials (user1:password):")
    response = requests.get(
        f"{BASE_URL}/basic-protected",
        auth=("user1", "password")
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")
    
    # With invalid credentials
    print("3. With invalid credentials:")
    response = requests.get(
        f"{BASE_URL}/basic-protected",
        auth=("user1", "wrongpassword")
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json() if response.status_code != 200 else response.text}\n")


def test_jwt_login():
    """Test JWT Login"""
    print("="*60)
    print("TESTING JWT LOGIN")
    print("="*60 + "\n")
    
    # Valid login
    print("1. Valid login (user1:password):")
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": "user1", "password": "password"}
    )
    print(f"Status: {response.status_code}")
    token_data = response.json()
    print(f"Response: {json.dumps(token_data, indent=2)}")
    
    if "access_token" in token_data:
        user_token = token_data["access_token"]
        print(f"Token: {user_token[:50]}...\n")
    else:
        user_token = None
    
    # Invalid login
    print("2. Invalid login (user1:wrongpassword):")
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": "user1", "password": "wrongpassword"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # Admin login
    print("3. Admin login (admin1:password):")
    response = requests.post(
        f"{BASE_URL}/login",
        json={"username": "admin1", "password": "password"}
    )
    print(f"Status: {response.status_code}")
    admin_token_data = response.json()
    print(f"Response: {json.dumps(admin_token_data, indent=2)}")
    
    if "access_token" in admin_token_data:
        admin_token = admin_token_data["access_token"]
        print(f"Token: {admin_token[:50]}...\n")
    else:
        admin_token = None
    
    return user_token, admin_token


def test_jwt_protected(user_token, admin_token):
    """Test JWT Protected Routes"""
    print("="*60)
    print("TESTING JWT PROTECTED ROUTES")
    print("="*60 + "\n")
    
    # Without token
    print("1. Access /jwt-protected WITHOUT token:")
    response = requests.get(f"{BASE_URL}/jwt-protected")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # With invalid token
    print("2. Access /jwt-protected WITH invalid token:")
    headers = {"Authorization": "Bearer invalid_token_here"}
    response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # With valid user token
    if user_token:
        print("3. Access /jwt-protected WITH valid user token:")
        headers = {"Authorization": f"Bearer {user_token}"}
        response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}\n")


def test_admin_only(user_token, admin_token):
    """Test Admin-Only Routes"""
    print("="*60)
    print("TESTING ADMIN-ONLY ROUTES")
    print("="*60 + "\n")
    
    # Without token
    print("1. Access /admin-only WITHOUT token:")
    response = requests.get(f"{BASE_URL}/admin-only")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # With user token
    if user_token:
        print("2. Access /admin-only WITH user token (non-admin):")
        headers = {"Authorization": f"Bearer {user_token}"}
        response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")
    
    # With admin token
    if admin_token:
        print("3. Access /admin-only WITH admin token:")
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}\n")


def test_home():
    """Test home endpoint"""
    print("="*60)
    print("API HOME ENDPOINT")
    print("="*60 + "\n")
    
    response = requests.get(f"{BASE_URL}/")
    print(json.dumps(response.json(), indent=2))
    print()


if __name__ == "__main__":
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "     Security API Test Suite - Flask-HTTPAuth & JWT".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")
    print()
    
    try:
        test_home()
        test_basic_auth()
        user_token, admin_token = test_jwt_login()
        test_jwt_protected(user_token, admin_token)
        test_admin_only(user_token, admin_token)
        
        print("="*60)
        print("All tests completed!")
        print("="*60)
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to Flask server.")
        print("Make sure the Flask app is running:")
        print("  python3 task_05_basic_security.py")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
