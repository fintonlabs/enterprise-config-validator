import os
import json
import yaml
from typing import Dict, List, Union
from jsonschema import validate, ValidationError
from jsonschema.exceptions import SchemaError


class Error:
    """
    Class representing an error in a configuration file.
    """

    def __init__(self, line: int, error_type: str, message: str):
        self.line = line
        self.error_type = error_type
        self.message = message


class ConfigurationFile:
    """
    Class representing a configuration file.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.format = self._get_file_format()
        self.content = self._load_file()
        self.errors = []

    def _get_file_format(self) -> str:
        _, ext = os.path.splitext(self.file_path)
        return ext[1:]

    def _load_file(self) -> Union[Dict, List]:
        try:
            with open(self.file_path, 'r') as file:
                if self.format == 'json':
                    return json.load(file)
                elif self.format == 'yaml':
                    return yaml.safe_load(file)
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            self.errors.append(Error(e.lineno, 'syntax', str(e)))
            return None


class Schema:
    """
    Class representing a schema against which configuration files are validated.
    """

    def __init__(self, schema_path: str):
        self.schema = self._load_schema(schema_path)

    def _load_schema(self, schema_path: str) -> Dict:
        with open(schema_path, 'r') as file:
            return json.load(file)


class Validator:
    """
    Class for validating configuration files against a schema.
    """

    def __init__(self, schema: Schema):
        self.schema = schema
        self.report = {
            'total_files': 0,
            'files_with_errors': 0,
            'total_errors': 0,
            'files': []
        }

    def validate(self, config_files: List[ConfigurationFile]) -> Dict:
        for config_file in config_files:
            self.report['total_files'] += 1
            if config_file.content is not None:
                try:
                    validate(instance=config_file.content, schema=self.schema.schema)
                except (ValidationError, SchemaError) as e:
                    config_file.errors.append(Error(e.absolute_path, 'compliance', str(e)))
                    self.report['files_with_errors'] += 1
                    self.report['total_errors'] += 1
            self.report['files'].append(config_file)
        return self.report


def main():
    schema = Schema('schema.json')
    validator = Validator(schema)
    config_files = [ConfigurationFile(file) for file in ['config1.json', 'config2.yaml']]
    report = validator.validate(config_files)
    print(report)


if __name__ == '__main__':
    main()