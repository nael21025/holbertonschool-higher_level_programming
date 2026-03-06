#!/usr/bin/python3
"""Test script for Flask API - task_04_flask.py"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"


def test_root():
    """Test root endpoint"""
    print("Testing GET /")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")


def test_data():
    """Test data endpoint"""
    print("Testing GET /data")
    response = requests.get(f"{BASE_URL}/data")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_status():
    """Test status endpoint"""
    print("Testing GET /status")
    response = requests.get(f"{BASE_URL}/status")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}\n")


def test_add_user():
    """Test adding users"""
    print("Testing POST /add_user")
    
    # Add first user
    user1 = {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=user1)
    print(f"Add Jane - Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    
    # Add second user
    user2 = {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    response = requests.post(f"{BASE_URL}/add_user", json=user2)
    print(f"Add John - Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def test_get_user():
    """Test getting specific user"""
    print("Testing GET /users/<username>")
    
    # Get existing user
    response = requests.get(f"{BASE_URL}/users/jane")
    print(f"Get Jane - Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    
    # Get non-existing user
    response = requests.get(f"{BASE_URL}/users/nonexistent")
    print(f"Get Nonexistent - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_errors():
    """Test error handling"""
    print("Testing Error Handling")
    
    # Missing username
    print("1. Missing username:")
    response = requests.post(f"{BASE_URL}/add_user", 
                            json={"name": "Test", "age": 25})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # Duplicate username
    print("2. Duplicate username:")
    response = requests.post(f"{BASE_URL}/add_user",
                            json={"username": "jane", "name": "Jane2"})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    
    # Invalid JSON
    print("3. Invalid JSON (header mismatch):")
    response = requests.post(f"{BASE_URL}/add_user",
                            data="not json",
                            headers={"Content-Type": "application/json"})
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


if __name__ == "__main__":
    print("="*50)
    print("Flask API Test Suite")
    print("="*50 + "\n")
    
    try:
        test_root()
        test_status()
        test_data()
        test_add_user()
        test_data()  # Check updated data list
        test_get_user()
        test_errors()
        
        print("="*50)
        print("All tests completed!")
        print("="*50)
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to Flask server.")
        print("Make sure the Flask app is running:")
        print("  python3 task_04_flask.py")
    except Exception as e:
        print(f"ERROR: {e}")
