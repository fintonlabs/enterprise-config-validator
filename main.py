import json
import yaml
from jsonschema import validate, ValidationError
from typing import Dict, Any, List


class ConfigValidator:
    """
    A class used to validate configuration files in YAML and JSON formats.

    ...

    Attributes
    ----------
    schema : Dict[str, Any]
        a dictionary representing the JSON schema to validate the configuration files against

    Methods
    -------
    load_file(file_path: str) -> Dict[str, Any]:
        Reads and parses a configuration file in either YAML or JSON format.
    validate_file(file_path: str, custom_rules: Dict[str, Any]) -> List[str]:
        Validates a configuration file against the schema and custom rules.
    """

    def __init__(self, schema: Dict[str, Any]):
        """
        Constructs all the necessary attributes for the ConfigValidator object.

        Parameters
        ----------
            schema : Dict[str, Any]
                a dictionary representing the JSON schema to validate the configuration files against
        """
        self.schema = schema

    def load_file(self, file_path: str) -> Dict[str, Any]:
        """
        Reads and parses a configuration file in either YAML or JSON format.

        Parameters
        ----------
            file_path : str
                the path to the configuration file

        Returns
        -------
            config_data : Dict[str, Any]
                a dictionary representing the parsed configuration data
        """
        try:
            with open(file_path, 'r') as file:
                if file_path.endswith('.json'):
                    config_data = json.load(file)
                elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                    config_data = yaml.safe_load(file)
                else:
                    raise ValueError("Unsupported file type. Only YAML and JSON files are supported.")
                return config_data
        except Exception as e:
            raise SystemExit(e)

    def validate_file(self, file_path: str, custom_rules: Dict[str, Any]) -> List[str]:
        """
        Validates a configuration file against the schema and custom rules.

        Parameters
        ----------
            file_path : str
                the path to the configuration file
            custom_rules : Dict[str, Any]
                a dictionary representing the custom rules to validate the configuration data against

        Returns
        -------
            errors : List[str]
                a list of error messages if the configuration data fails validation, otherwise an empty list
        """
        config_data = self.load_file(file_path)
        errors = []

        # Validate against schema
        try:
            validate(instance=config_data, schema=self.schema)
        except ValidationError as e:
            errors.append(str(e))

        # Validate against custom rules
        for rule, value in custom_rules.items():
            if rule not in config_data or config_data[rule] != value:
                errors.append(f"Custom rule validation failed for rule '{rule}': Expected '{value}', got '{config_data.get(rule)}'")

        return errors


# Example usage
if __name__ == "__main__":
    # Define schema and custom rules
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "number"}
        },
        "required": ["name", "age"]
    }
    custom_rules = {"age": 30}

    # Create ConfigValidator instance
    validator = ConfigValidator(schema)

    # Validate files
    for file_path in ["config1.json", "config2.yaml"]:
        errors = validator.validate_file(file_path, custom_rules)
        if errors:
            print(f"Validation failed for '{file_path}' with the following errors:")
            for error in errors:
                print(f"- {error}")
        else:
            print(f"Validation passed for '{file_path}'")