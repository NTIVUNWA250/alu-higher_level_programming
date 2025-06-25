#!/usr/bin/python3
import importlib.util
import os
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pyc_path = os.path.join(current_dir, "hidden_4.pyc")
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)
    names = dir(hidden_module)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
