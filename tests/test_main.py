import unittest
from main import ConfigurationValidator

class TestConfigurationValidator(unittest.TestCase):
    def setUp(self):
        self.schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"}
            },
            "required": ["name", "age"]
        }
        self.validator = ConfigurationValidator(self.schema)

    def test_load_file(self):
        # Test loading a valid JSON file
        file_data = self.validator.load_file('tests/config.json')
        self.assertEqual(file_data, {'name': 'John Doe', 'age': 30})

        # Test loading a valid YAML file
        file_data = self.validator.load_file('tests/config.yaml')
        self.assertEqual(file_data, {'name': 'John Doe', 'age': 30})

        # Test loading a file with an unsupported format
        with self.assertRaises(ValueError):
            self.validator.load_file('tests/config.txt')

    def test_validate_file(self):
        # Test validating a valid file
        file_data = {'name': 'John Doe', 'age': 30}
        self.validator.validate_file(file_data)

        # Test validating an invalid file
        file_data = {'name': 'John Doe'}
        with self.assertRaises(ValidationError):
            self.validator.validate_file(file_data)

if __name__ == '__main__':
    unittest.main()