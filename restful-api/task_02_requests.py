#!/usr/bin/python3
"""Task 2: Consume and process data from an API using Python requests"""

import requests
import csv
import json


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print titles.
    
    This function:
    - Makes a GET request to JSONPlaceholder API
    - Checks the status code
    - Parses JSON response
    - Prints titles of all posts
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        # Print status code
        print(f"Status Code: {response.status_code}")
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON data
            posts = response.json()
            
            # Print title of each post
            for post in posts:
                print(post.get("title"))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder API and save to CSV file.
    
    This function:
    - Makes a GET request to JSONPlaceholder API
    - Parses JSON response
    - Extracts id, title, and body
    - Writes data to posts.csv file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json()
            
            # Create list of dictionaries with id, title, body
            posts_data = [
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                }
                for post in posts
            ]
            
            # Write to CSV file
            if posts_data:
                # Get keys from first post dictionary
                fieldnames = posts_data[0].keys()
                
                # Write CSV file
                with open("posts.csv", mode="w", newline="", encoding="utf-8") as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    
                    # Write header
                    writer.writeheader()
                    
                    # Write all posts
                    writer.writerows(posts_data)
                
                print(f"Successfully saved {len(posts_data)} posts to posts.csv")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")


if __name__ == "__main__":
    # Run both functions
    fetch_and_print_posts()
    print("\n" + "="*50 + "\n")
    fetch_and_save_posts()
