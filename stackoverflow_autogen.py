# Install Cookiecutter
!pip install cookiecutter

# Remove existing directory
!rm -rf stackoverflow_script

# Create template directory
!mkdir stackoverflow_script

# Create template files
!touch stackoverflow_script/cookiecutter.json
!touch stackoverflow_script/StackExplorer.py

# Write cookiecutter.json
import json
data = {
  "project_name": "",
  "stackoverflow_tag": ""
}
with open('stackoverflow_script/cookiecutter.json', 'w') as f:
  json.dump(data, f)

# Write StackExplorer.py
import requests
project_name = "StackExplorer"
stackoverflow_tag = "Python"
code = f"""
import requests

# Stack Overflow API endpoint
url = f"https://api.stackexchange.com/2.3/questions"

# Parameters
params = {{
    "site": "stackoverflow",
    "tagged": "{stackoverflow_tag}",
    "pagesize": 10
}}

response = requests.get(url, params=params)
data = response.json()

# Print questions
for question in data["items"]:
    print(question["title"])
"""
with open('stackoverflow_script/StackExplorer.py', 'w') as f:
  f.write(code)

# Run generated script
!python stackoverflow_script/StackExplorer.py
