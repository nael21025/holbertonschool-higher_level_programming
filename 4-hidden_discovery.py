#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Load the compiled module
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Get all names that do not start with __
        names = [name for name in dir(module) if not name.startswith("__")]
        # Sort alphabetically
        names.sort()
        # Print one per line
        for name in names:
            print(name)
    else:
        print("Cannot load the module")