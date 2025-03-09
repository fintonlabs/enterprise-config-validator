# The code should be able to read and validate enterprise configuration files in YAML and JSON formats


## Table of Contents

- [📋 Table of Contents](#📋-table-of-contents)
- [1. Prerequisites](#1.-prerequisites)
- [2. Installation Process](#2.-installation-process)
- [3. Verification Steps](#3.-verification-steps)
- [4. Post-Installation Configuration](#4.-post-installation-configuration)
- [Usage Guide](#usage-guide)
- [Class Description](#class-description)
- [Attributes](#attributes)
- [Methods](#methods)
- [Common Patterns and Best Practices](#common-patterns-and-best-practices)
- [⚙️ Configuration](#⚙️-configuration)
- [🔍 Troubleshooting](#🔍-troubleshooting)
- [🤝 Contributing](#🤝-contributing)
- [📄 License](#📄-license)
- [Features](#features)
- [API Documentation](#api-documentation)
# Project Overview

This project involves constructing a Python-based code that provides validation for enterprise-level configuration files in YAML and JSON formats. The ability to validate these types of files is crucial in maintaining the integrity and consistency of configurations across multiple systems in a given enterprise. The code constitutes a class, `ConfigurationValidator`, that can load these files, parse them into a dictionary, and validate them against a given schema.

The utility of this project is particularly pronounced in large-scale systems where configuration files are ubiquitous and their correctness is paramount. By enabling automated syntax checking and compliance validation, this project aids in preventing potential configuration errors, thus ensuring smooth operation of systems and applications.

# Features

- 📂 **File Loading**: The `load_file(file_path: str) -> Dict[str, Any]` method loads a configuration file from a specified path. The file can be either YAML or JSON format. This method parses the file contents and returns them as a dictionary, which can then be processed or validated further.

- 🧾 **File Validation**: The `validate_file(file_data: Dict[str, Any]) -> None` method checks the loaded configuration data against a specified schema. This ensures that your configuration data adheres to a particular structure and contains all of the necessary fields, helping to prevent errors or inconsistencies in your configurations.

- 💼 **Schema Management**: The `ConfigurationValidator` class allows the user to specify a validation schema upon instantiation. This schema is then used for subsequent validations. This feature provides flexibility, as it allows users to easily change the schema based on their requirements.

- ❌ **Error Handling**: The application uses the `jsonschema` library's `ValidationError` to effectively handle errors during the validation process. If a configuration file fails to meet the schema requirements, a `ValidationError` is raised, providing useful feedback to the user.

- 🔄 **Support for YAML and JSON**: This code supports both YAML and JSON formats, two of the most popular data serialization languages used in configuration files. By supporting these formats, the code caters to a wide variety of configuration management needs.

- 📝 **Type Hinting**: The use of type hinting throughout the code makes it much easier to understand what type of data each function expects and returns. This can be especially useful for other developers who may need to modify or extend the code.

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

# Installation Guide for ConfigurationValidator Project

This guide provides comprehensive instructions on how to install and set up the ConfigurationValidator project.

## 1. Prerequisites

Before starting the installation process, ensure that you have the following software installed on your system:

- Python 3.6 or higher: The ConfigurationValidator project is built on Python. You can download it from the [official Python website](https://www.python.org/downloads/).
- pip: This is the package installer for Python. It comes bundled with Python 3.4 and above.

Additionally, the project has the following Python dependencies:

- PyYAML: A Python library for parsing YAML.
- jsonschema: A Python library for validating JSON data.

## 2. Installation Process

Follow the steps below to install the ConfigurationValidator project:

1. **Clone the repository**

   Open your terminal and run the following command to clone the project repository:

   ```bash
   git clone https://github.com/username/ConfigurationValidator.git
   ```

   Replace `username` with the actual username of the repository owner.

2. **Navigate to the project directory**

   Use the `cd` command to navigate into the cloned repository:

   ```bash
   cd ConfigurationValidator
   ```

3. **Create a virtual environment (optional)**

   It is recommended to create a virtual environment to isolate the project dependencies. Use the following commands to create and activate a new virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. **Install the dependencies**

   Run the following command to install the required Python libraries:

   ```bash
   pip install pyyaml jsonschema
   ```

## 3. Verification Steps

To verify that the project has been installed correctly:

1. Run the Python interpreter in the terminal:

   ```bash
   python3
   ```

2. Import the `ConfigurationValidator` class:

   ```python
   from ConfigurationValidator import ConfigurationValidator
   ```

   If the command runs without throwing any errors, the project has been installed successfully.

## 4. Post-Installation Configuration

After successful installation, you may need to define your own schema for the ConfigurationValidator. The schema is a dictionary representing the validation rules for your specific configuration files.

Here's a simple example of how to define a schema and use the `ConfigurationValidator`:

```python
schema = {
    "type" : "object",
    "properties" : {
        "price" : {"type" : "number"},
        "name" : {"type" : "string"},
    },
}

validator = ConfigurationValidator(schema)
config = validator.load_file('config.yaml')
validator.validate_file(config)
```

Remember to replace `'config.yaml'` with the path to your actual configuration file.

That's it! You've successfully installed and set up the ConfigurationValidator project. Enjoy validating your configuration files!

---

## Usage Guide

---

### 1. Basic Usage Examples

To use the `ConfigurationValidator` class, you first need to define your schema. The schema will be used to validate the configuration files.

```python
schema = {
  "type" : "object",
  "properties" : {
    "price" : {"type" : "number"},
    "name" : {"type" : "string"},
  },
}
```
Next, you can instantiate the `ConfigurationValidator` class with your schema.

```python
validator = ConfigurationValidator(schema)
```
To load and validate a configuration file, you can use the `load_file` and `validate_file` methods.

```python
file_data = validator.load_file('config.yaml')
validator.validate_file(file_data)
```

---

### 2. Common Use Cases

The most common use case for this code is the validation of configuration files in enterprise applications. 

For example, if you have a system that relies on configuration files to set some parameters, you can use this class to make sure that the files are correctly formatted and comply with your requirements.

---

### 3. Command-Line Arguments or Parameters

This code is intended to be used in a larger Python application, so there are no command-line arguments or parameters.

---

### 4. Expected Output Examples

If the configuration file is valid according to the schema, the `validate_file` method will not return anything. 

However, if it's invalid, the method will raise a `jsonschema.exceptions.ValidationError` exception.

```python
try:
    validator.validate_file(file_data)
except ValidationError as e:
    print(f'Invalid configuration file: {e.message}')
```
In the above code, if the configuration file is invalid, the program will print a message like this:

```
Invalid configuration file: 'price' is a required property
```

---

### 5. Advanced Usage Scenarios

For advanced usage, you can modify the schema according to your needs. The schema must comply with the [JSON Schema specification](https://json-schema.org/).

For example, you can add more complex validation rules. The following schema requires the `price` property to be a number greater than or equal to 0 and the `name` property to be a string with a minimum length of 1.

```python
schema = {
  "type" : "object",
  "properties" : {
    "price" : {
      "type" : "number",
      "minimum" : 0
    },
    "name" : {
      "type" : "string",
      "minLength" : 1
    },
  },
  "required": ["price", "name"]
}
```

You can also use the `jsonschema` library's functions for more advanced validation scenarios. Please refer to the [jsonschema documentation](https://python-jsonschema.readthedocs.io/en/latest/) for more information.

# ConfigurationValidator Class API Documentation

This documentation covers the `ConfigurationValidator` class in the enterprise configuration file validation project. This class is used to read and validate configuration files in YAML and JSON formats.

## Class Description

`ConfigurationValidator` is a Python class that validates configuration files in JSON and YAML formats. It checks and validates the syntax and compliance of the configuration files against a provided schema.

## Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `schema` | dict | A dictionary representing the validation schema against which the configuration files are validated. |

## Methods

### 1. `__init__(self, schema: Dict[str, Any]) -> None`

This is the constructor method for the `ConfigurationValidator` class.

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `schema` | dict | A dictionary representing the validation schema. |

**Return Value**

This method does not return any value.

**Code example**

```python
schema = {"type" : "object", "properties" : {"name" : {"type" : "string"}}}
validator = ConfigurationValidator(schema)
```

### 2. `load_file(self, file_path: str) -> Dict[str, Any]`

This method loads a configuration file and returns it as a dictionary.

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `file_path` | str | The path to the configuration file to be loaded. |

**Return Value**

Returns a dictionary representing the configuration file.

**Code example**

```python
config_file = validator.load_file('/path/to/config/file')
```

### 3. `validate_file(self, file_data: Dict[str, Any]) -> None`

This method validates a configuration file against the schema. If the file is not compliant with the schema, a `ValidationError` exception is raised.

**Parameters**

| Parameter | Type | Description |
| --- | --- | --- |
| `file_data` | dict | A dictionary representing the configuration file to be validated. |

**Return Value**

This method does not return any value.

**Code example**

```python
try:
    validator.validate_file(config_file)
except ValidationError as e:
    print(f"Validation error: {e.message}")
```

## Common Patterns and Best Practices

- Always provide a valid JSON schema while creating an instance of ConfigurationValidator.
- Use `load_file` method to load the configuration file before validating it with `validate_file`.
- Always use a try-except block while validating the file to handle potential `ValidationError` exceptions.

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
