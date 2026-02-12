#!/usr/bin/python3
"""Convert CSV to JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
        Convert CSV data to JSON format
        - csv_filename: The CSV file to convert
        Returns: True if successful, False otherwise
    """
    try:
        data = []
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
