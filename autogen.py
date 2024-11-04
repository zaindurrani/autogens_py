# Install Cookiecutter, a popular autogen tool
!pip install cookiecutter

# Remove existing directory to avoid conflicts
!rm -rf script_generator

# Create a new directory for the generated script
!mkdir script_generator

# Create template files for Cookiecutter
!touch script_generator/cookiecutter.json
!touch script_generator/script.py

# Get user input for script details
script_name = input("Enter script name: ")
script_description = input("Enter script description: ")
script_type = input("Enter script type (e.g., web scraper, data analyzer): ")

# Write cookiecutter.json with user input
import json
data = {
  "script_name": script_name,
  "script_description": script_description,
  "script_type": script_type
}
with open('script_generator/cookiecutter.json', 'w') as f:
  json.dump(data, f)

# Write script.py with a basic template
code = f"""
# {script_name} - {script_description}
# {script_type} script

import requests

def main():
  # TO DO: Implement {script_type} logic here
  print("Script running...")
  # Example: Make a GET request
  response = requests.get("https://www.example.com")
  print(response.status_code)

if __name__ == "__main__":
  main()
"""
with open('script_generator/script.py', 'w') as f:
  f.write(code)

# Run the generated script using Python
!python script_generator/script.py
