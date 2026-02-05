# Python - Inheritance

## Learning Objectives

This project covers the fundamentals of Object-Oriented Programming (OOP) with a focus on inheritance in Python:

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- When and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.

### 1. My list
Write a class `MyList` that inherits from `list` with a `print_sorted()` method.

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class.

### 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

### 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited from the specified class.

### 5. Geometry module
Write an empty class `BaseGeometry`.

### 6. Improve Geometry
Add an `area()` method to `BaseGeometry` that raises an `Exception`.

### 7. Integer validator
Add an `integer_validator()` method to validate parameters.

### 8. Rectangle
Write a `Rectangle` class that inherits from `BaseGeometry`.

### 9. Full rectangle
Improve the `Rectangle` class with area calculation and string representation.

### 10. Square #1
Write a `Square` class that inherits from `Rectangle`.

### 11. Square #2
Improve the `Square` class with custom string representation.

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Code follows pycodestyle (version 2.7.*)
- All files must be executable
- No modules are imported unless necessary

### Documentation
- All modules have documentation
- All classes have documentation
- All functions have documentation
- Documentation is a real sentence explaining the purpose
- No use of the words "import" or "from" in comments

## Usage

Test files can be run using:
```bash
python3 -m doctest ./tests/*
```

Or test individual files:
```bash
python3 [file_name]-main.py
```

## Author

School project for learning Python inheritance concepts.
