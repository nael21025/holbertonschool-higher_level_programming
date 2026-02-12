#!/usr/bin/python3
"""11 Student to disk and reload"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """
            Initializes a Student instance
             - first_name: first name of the student
             - last_name: last name of the student
             - age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Get the JSON representation of a Student instance
             - attrs: list of attributes to represent in the JSON output
        """
        if type(attrs) is not list:
            return self.__dict__

        _dict = {}
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
            if i in self.__dict__:
                _dict[i] = self.__dict__[i]

        return _dict

    def reload_from_json(self, json):
        """
            Replaces all attributes of the Student instance.
            Arguments:
                json (dict): To replace.
        """
        for key in json:
            val = json[key]
            setattr(self, key, val)
