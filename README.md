# AUTOGENS


# Autogen Script Generator

## What are Autogens?

Autogens, short for "automatic generators," are tools that create code, files, or projects based on user input or templates. They streamline development processes, reducing manual effort and increasing productivity.

## How are Autogens used?

Autogens are commonly used in:

1. Web development: generating HTML, CSS, and JavaScript files
2. Software development: creating boilerplate code, classes, or functions
3. Data science: generating data analysis scripts or visualization code
4. DevOps: automating infrastructure provisioning and configuration

## What does this code do?

This code uses Cookiecutter, a popular autogen tool, to generate a Python script based on user input. The script includes:

1. User-provided script name, description, and type
2. A basic template with a `main` function and example `requests` library call
3. A `cookiecutter.json` file storing user input

The generated script is stored in the `script_generator` directory and can be modified to suit specific needs.

## Requirements

* Google Colab or Jupyter Notebook environment
* Cookiecutter installed (`!pip install cookiecutter`)

## Usage

1. Run the code in Colab or Jupyter Notebook
2. Provide script name, description, and type when prompted
3. Find the generated script in the `script_generator` directory
4. Modify and run the script as needed
