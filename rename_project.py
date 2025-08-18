#!/usr/bin/env python3
"""Utility to rename FaceFusion project.

Asks the user for a new project name and replaces all occurrences of
"facefusion" in text files within the repository with the provided name.
File contents only are modified; file and directory names remain unchanged.
"""
import os
import sys

def replace_occurrences(root: str, old: str, new: str) -> None:
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except (UnicodeDecodeError, OSError):
                continue
            new_content = content.replace(old, new)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    new_name = input("Enter new project name: ").strip()
    if not new_name:
        print("No name provided; aborting.")
        sys.exit(1)
    replace_occurrences('.', 'facefusion', new_name)
    print(f"Replaced 'facefusion' with '{new_name}'.")
