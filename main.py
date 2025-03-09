import json
import yaml
import jsonschema
from typing import Dict, Any
from jsonschema import validate, ValidationError


class ConfigurationValidator:
    """
    A class used to validate configuration files in JSON and YAML formats.

    Attributes
    ----------
    schema : dict
        a dictionary representing the validation schema

    Methods
    -------
    load_file(file_path: str) -> Dict[str, Any]
        loads a configuration file and returns it as a dictionary
    validate_file(file_data: Dict[str, Any]) -> None
        validates a configuration file against the schema
    """

    def __init__(self, schema: Dict[str, Any]) -> None:
        """
        Constructs all the necessary attributes for the ConfigurationValidator object.

        Parameters
        ----------
        schema : dict
            a dictionary representing the validation schema
        """
        self.schema = schema

    def load_file(self, file_path: str) -> Dict[str, Any]:
        """
        Loads a configuration file and returns it as a dictionary.

        Parameters
        ----------
        file_path : str
            the path of the configuration file

        Returns
        -------
        dict
            a dictionary representing the configuration file
        """
        try:
            if file_path.endswith('.json'):
                with open(file_path, 'r') as file:
                    return json.load(file)
            elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                with open(file_path, 'r') as file:
                    return yaml.safe_load(file)
            else:
                raise ValueError('Unsupported file format. Only JSON and YAML files are supported.')
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            print(f'Syntax error in file {file_path}: {e}')
            return {}
        except FileNotFoundError as e:
            print(f'File not found: {file_path}')
            return {}

    def validate_file(self, file_data: Dict[str, Any]) -> None:
        """
        Validates a configuration file against the schema.

        Parameters
        ----------
        file_data : dict
            a dictionary representing the configuration file

        Raises
        ------
        ValidationError
            if the configuration file does not comply with the schema
        """
        try:
            validate(instance=file_data, schema=self.schema)
            print('File is valid.')
        except ValidationError as e:
            print(f'Compliance error: {e.message}')


# Example usage
if __name__ == "__main__":
    # Define a simple schema for demonstration purposes
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["name", "age"]
    }

    validator = ConfigurationValidator(schema)

    # Load and validate a JSON file
    file_data = validator.load_file('config.json')
    validator.validate_file(file_data)

    # Load and validate a YAML file
    file_data = validator.load_file('config.yaml')
    validator.validate_file(file_data)