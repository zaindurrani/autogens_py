AutoGen using Hugging Face

Automatically generate Python scripts using Hugging Face's Transformers API.

Table of Contents

1. #overview
2. #requirements
3. #usage
4. #api-settings
5. #cookiecutter-settings
6. #retry-mechanism
7. #troubleshooting

Overview

AutoGen uses Hugging Face's Transformers API to generate Python scripts based on user input.

Requirements

- Python 3.7+
- requests library (pip install requests)
- Hugging Face API access (sign up for free)

Usage

1. Run the script.
2. Enter a script description when prompted.
3. The script will generate a Python script based on the description.
4. The generated script will be written to script_generator/script.py.
5. The script will attempt to run the generated script.

API Settings

- API URL: https://api-inference.huggingface.co/models/transformers/parse
- API Parameters:
    - inputs: User-provided script description.
    - parameters:
        - return_code: True
        - stop_sequences: ["\n"]

Cookiecutter Settings

- Directory: script_generator

Retry Mechanism

- Max retries: 5
- Delay between retries: 1 minute

Troubleshooting

- Rate limit exceeded: Wait 1 minute and retry.
- API request failed: Check API status code and error message.

Code


import os
import json
import requests
import time

# Hugging Face API settings
api_url = "https://api-inference.huggingface.co/models/transformers/parse"

# Cookiecutter settings
cookiecutter_dir = "script_generator"

# Get script description from user
description = input("Enter script description: ")

# Prepare API request
data = {
    "inputs": description,
    "parameters": {
        "return_code": True,
        "stop_sequences": ["\n"]
    }
}

# Retry mechanism
retries = 0
max_retries = 5
delay = 60  # 1 minute

while retries < max_retries:
    # Send API request
    response = requests.post(api_url, json=data)

    # Check response status code
    if response.status_code == 200:
        # Process API response
        try:
            response_json = response.json()
            print("API Response:")
            print(response_json)

            # Check if 'generated' key exists
            if 'generated' in response_json:
                script = response_json['generated']
            elif 'error' in response_json:
                print("API Error:")
                print(response_json['error'])
            else:
                print("Unknown API response format.")
                print(response_json)

            # Create script directory
            os.makedirs(cookiecutter_dir, exist_ok=True)

            # Write script to file
            with open(os.path.join(cookiecutter_dir, "script.py"), "w") as f:
                f.write(script)

            # Run generated script
            !python script_generator/script.py
            break
        except Exception as e:
            print("Error parsing API response:")
            print(str(e))
            break
    elif response.status_code == 429:
        print("Rate limit exceeded. Retrying...")
        retries += 1
        time.sleep(delay)
    else:
        print(f"API request failed with status code {response.status_code}")
        break
