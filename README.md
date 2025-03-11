# The code should be able to read and validate enterprise configuration files in YAML and JSON formats


## Table of Contents

- [📋 Table of Contents](#📋-table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation Process](#installation-process)
- [Verification](#verification)
- [Post-Installation Configuration](#post-installation-configuration)
- [1. Basic Usage](#1.-basic-usage)
- [2. Common Use Cases](#2.-common-use-cases)
- [3. Command-line Arguments](#3.-command-line-arguments)
- [4. Expected Output Examples](#4.-expected-output-examples)
- [5. Advanced Usage Scenarios](#5.-advanced-usage-scenarios)
- [Class: ConfigValidator](#class:-configvalidator)
- [⚙️ Configuration](#⚙️-configuration)
- [🔍 Troubleshooting](#🔍-troubleshooting)
- [🤝 Contributing](#🤝-contributing)
- [📄 License](#📄-license)
- [Features](#features)
- [API Documentation](#api-documentation)
# Project Overview

The project provides a robust solution for validating enterprise configuration files in YAML and JSON formats. This validation is crucial in maintaining the integrity of configuration files, ensuring that they are not only syntactically correct but also compliant with predefined rules. By employing this project, developers and system administrators can prevent potential system crashes or malfunctions due to incorrect or non-compliant configuration files.

# Features 

- **File Reading and Parsing** :open_book: :arrow_right: :floppy_disk:
  
  The `load_file()` method reads and parses a configuration file in either YAML or JSON format, ensuring that the file is in a format that can be validated against the schema. By supporting both YAML and JSON formats, the project accommodates the most commonly used formats for configuration files in modern development environments.

- **JSON Schema Validation** :clipboard: :heavy_check_mark:

  The project uses the `jsonschema` library to validate configuration files against a predefined JSON schema. The `validate_file()` method checks the configuration files against this schema, ensuring that they are not only syntactically correct but also adhere to the structure defined by the schema.

- **Custom Rules Validation** :wrench: :heavy_check_mark:

  In addition to schema validation, the project also supports validation against custom rules. The `validate_file()` method allows users to specify a dictionary of custom rules that the configuration file should comply with. This feature provides an extra layer of customization and control, allowing users to enforce specific rules that are not covered by the JSON schema.

- **Error Reporting** :x: :loudspeaker:

  When the `validate_file()` method encounters syntax or compliance errors in the configuration files, it reports these errors back to the user. This feature allows users to quickly identify and rectify issues in their configuration files, minimizing downtime and potential system malfunctions.

- **Ease of Use** :grinning: :thumbsup:

  The project is implemented as a class, `ConfigValidator`, which can be easily instantiated and used in any Python code. By passing the JSON schema to the constructor, users can create a validator object and use it to validate any number of configuration files. This design makes the project highly reusable and easy to integrate into existing codebases.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation Instructions

This document provides step-by-step instructions on how to install and configure the ConfigValidator project on your system.

## Prerequisites

Before proceeding with the installation process, ensure that you have the following software and dependencies installed on your system:

1. **Python 3.6 or higher**: The project is written in Python. If you don't have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

2. **Pip**: Pip is a package manager for Python. It is used to install and manage Python packages. It usually comes with Python. If not, follow this [guide](https://pip.pypa.io/en/stable/installing/) to install it.

3. **Virtualenv (Optional)**: Virtualenv is a tool to create isolated Python environments. It's not mandatory but recommended to avoid conflicts with other Python projects. Install it using pip: `pip install virtualenv`

4. **Dependencies**: This project relies on the following libraries:
   - `PyYAML`: A YAML parser and emitter for Python.
   - `jsonschema`: An implementation of JSON Schema for Python.
   
To save time, these dependencies will be installed during the installation process of the project.

## Installation Process

Follow these steps to install the ConfigValidator project:

1. **Clone the repository**: Use git to clone the repository. Replace `<URL>` with the URL of the repository.

   ```
   git clone <URL>
   ```
   
2. **Navigate to the project directory**:

   ```
   cd ConfigValidator
   ```

3. **Create a virtual environment (Optional)**: If you've installed virtualenv, create a new environment and activate it:

   ```
   virtualenv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the dependencies**: Use pip to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Verification

To ensure the ConfigValidator project has been installed successfully, try importing the ConfigValidator class in python:

1. Start a Python interpreter:

   ```
   python
   ```

2. Import the ConfigValidator class:

   ```python
   from ConfigValidator import ConfigValidator
   ```

3. If you don't see any import errors, the installation was successful.

## Post-Installation Configuration

After successful installation, you need to provide a JSON schema that will be used to validate configuration files. This schema should be passed as a dictionary when creating a ConfigValidator object:

```python
schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}

validator = ConfigValidator(schema)
 ```

Now, you're all set to start validating your configuration files with the ConfigValidator project.

# Usage Guide for ConfigValidator

This guide provides a detailed overview of how to use the `ConfigValidator` class, which validates JSON and YAML enterprise configuration files.

## 1. Basic Usage

The `ConfigValidator` class validates configuration files against a provided JSON schema. Below is a basic usage example:

```python
schema = {
    "type" : "object",
    "properties" : {
        "url" : {"type" : "string"},
        "port" : {"type" : "number"}
    },
    "required": ["url", "port"]
}

validator = ConfigValidator(schema)

config_file = '/path/to/config.yaml'
custom_rules = {"url": "https://example.com", "port": 8080}

validator.validate_file(config_file, custom_rules)
```

## 2. Common Use Cases

### 2.1. Validating Configuration Files

To validate a configuration file against the provided schema and custom rules, use the `validate_file()` method:

```python
errors = validator.validate_file(config_file, custom_rules)
if errors:
    print(f'Validation errors: {errors}')
else:
    print('Validation successful')
```

### 2.2. Reading Configuration Files

To read and parse a configuration file without validation, use the `load_file()` method:

```python
config_data = validator.load_file(config_file)
print(config_data)
```

## 3. Command-line Arguments

The `ConfigValidator` class is designed to be used within a Python script. It does not accept command-line arguments directly, but you can design your script to accept arguments and pass them to the `ConfigValidator`.

## 4. Expected Output Examples

The `validate_file()` method returns a list of error messages if the configuration file fails validation. If the file passes validation, it returns an empty list.

Example:

```python
errors = validator.validate_file(config_file, custom_rules)
print(errors)
# Output: ['url: https://example.com does not match expected value', 'port: 8080 does not match expected value']
```

The `load_file()` method returns a dictionary with the contents of the configuration file.

Example:

```python
config_data = validator.load_file(config_file)
print(config_data)
# Output: {'url': 'https://example.com', 'port': 8080}
```

## 5. Advanced Usage Scenarios

For advanced use cases, `ConfigValidator` can be extended to add more specific validation rules or methods. For example, to add a method that checks if a URL in the configuration file is reachable:

```python
import requests

class AdvancedConfigValidator(ConfigValidator):
    def is_url_reachable(self, url):
        try:
            response = requests.get(url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

adv_validator = AdvancedConfigValidator(schema)
config_data = adv_validator.load_file(config_file)

if adv_validator.is_url_reachable(config_data['url']):
    print('URL is reachable')
else:
    print('URL is not reachable')
```
This advanced usage scenario demonstrates how versatile the `ConfigValidator` class can be, able to be tailored to your specific needs.

# ConfigValidator Library API Documentation

## Class: ConfigValidator

The `ConfigValidator` class is used to validate configuration files in YAML and JSON formats.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `schema`  | `Dict[str, Any]` | A dictionary representing the JSON schema to validate the configuration files against. |

### Methods

#### `__init__(self, schema: Dict[str, Any]) -> None`

This method is used to construct all the necessary attributes for the `ConfigValidator` object.

| Parameter | Type | Description |
|-----------|------|-------------|
| `schema`  | `Dict[str, Any]` | A dictionary representing the JSON schema to validate the configuration files against. |

**Example:**

```python
schema = {
    "type" : "object",
    "properties" : {
        "name" : {"type" : "string"},
        "age" : {"type" : "number"},
    },
}
validator = ConfigValidator(schema)
```

#### `load_file(self, file_path: str) -> Dict[str, Any]`

This method reads and parses a configuration file in either YAML or JSON format.

| Parameter | Type | Description |
|-----------|------|-------------|
| `file_path` | `str` | The path to the configuration file to be loaded. |

**Returns:**

A dictionary representing the loaded configuration file.

**Example:**

```python
config = validator.load_file("/path/to/config.yaml")
```

#### `validate_file(self, file_path: str, custom_rules: Dict[str, Any]) -> List[str]`

This method validates a configuration file against the schema and custom rules.

| Parameter | Type | Description |
|-----------|------|-------------|
| `file_path` | `str` | The path to the configuration file to be validated. |
| `custom_rules` | `Dict[str, Any]` | A dictionary representing the custom rules to be applied during validation. |

**Returns:**

A list of strings representing any validation errors found. If the list is empty, it means the configuration file is valid.

**Example:**

```python
errors = validator.validate_file("/path/to/config.json", {
    "name": {"type": "string", "minLength": 5},
    "age": {"type": "number", "minimum": 18},
})
if errors:
    print("Validation errors:", errors)
else:
    print("Configuration file is valid.")
```

### Common Patterns and Best Practices

- Always specify a comprehensive schema when instantiating the `ConfigValidator` class. This schema should cover all the fields expected in the configuration files and their respective types.

- Use the `load_file` method to load configuration files before attempting to validate them.

- Specify custom validation rules when calling the `validate_file` method to enforce additional requirements beyond those specified in the schema.

- Always handle the list of validation errors returned by the `validate_file` method. An empty list signifies a valid configuration file, while a non-empty list contains the error messages for each validation error found.

## ⚙️ Configuration
Configuration options for customizing the application's behavior.

## 🔍 Troubleshooting
Common issues and their solutions.

## 🤝 Contributing
Guidelines for contributing to the project.

## 📄 License
This project is licensed under the MIT License.

## Features

- Complete feature 1: Detailed description
- Complete feature 2: Detailed description
- Complete feature 3: Detailed description

## API Documentation

### Endpoints

#### `GET /api/resource`

Returns a list of resources.

**Parameters:**

- `limit` (optional): Maximum number of resources to return

**Response:**

```json
{
  "resources": [
    {
      "id": 1,
      "name": "Resource 1"
    }
  ]
}
```
