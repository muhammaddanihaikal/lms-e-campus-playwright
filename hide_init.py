import os
import subprocess

def hide_init_files():
    """Hide all __init__.py files except in .venv"""
    for root, dirs, files in os.walk('.'):
        # Skip .venv directory
        if '.venv' in root:
            continue

        for file in files:
            if file == '__init__.py':
                filepath = os.path.join(root, file)
                try:
                    # Use attrib command to hide file
                    result = subprocess.run(['attrib', '+h', filepath], capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"Hidden: {filepath}")
                    else:
                        print(f"Failed: {filepath} - {result.stderr}")
                except Exception as e:
                    print(f"Error: {filepath} - {e}")

if __name__ == "__main__":
    hide_init_files()
