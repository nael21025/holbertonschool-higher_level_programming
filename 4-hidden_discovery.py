#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    # Load the compiled module
    with open('/tmp/hidden_4.pyc', 'rb') as f:
        f.read(12)  # Skip the header (magic 4, mtime 4, size 4)
        code = marshal.load(f)
    
    # Create a module object
    module = types.ModuleType('hidden_4')
    module.__dict__.update({'__name__': 'hidden_4', '__file__': '/tmp/hidden_4.pyc'})
    
    # Execute the code in the module's namespace
    exec(code, module.__dict__)
    
    # Get all names that do not start with __
    names = [name for name in dir(module) if not name.startswith("__")]
    # Sort alphabetically
    names.sort()
    # Print one per line
    for name in names:
        print(name)