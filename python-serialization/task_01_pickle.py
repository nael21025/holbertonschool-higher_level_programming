#!/usr/bin/python3
"""Custom object serialization with pickle"""
import pickle


class CustomObject:
    """Custom object class"""

    def __init__(self, name, age, is_student):
        """
            Initialize a CustomObject instance
            - name: a string
            - age: an integer
            - is_student: a boolean
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
            Serialize the current instance to a file
            - filename: The file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
            Deserialize an instance from a file
            - filename: The file to load the instance from
            Returns: A CustomObject instance or None
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
