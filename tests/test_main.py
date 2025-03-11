import unittest
from main import ConfigValidator

class TestConfigValidator(unittest.TestCase):
    def setUp(self):
        self.validator = ConfigValidator({
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"}
            },
            "required": ["name", "age"]
        })

    def test_load_file(self):
        # Test loading a valid JSON file
        data = self.validator.load_file('tests/test.json')
        self.assertEqual(data, {"name": "John", "age": 30})

        # Test loading a valid YAML file
        data = self.validator.load_file('tests/test.yaml')
        self.assertEqual(data, {"name": "John", "age": 30})

        # Test loading an unsupported file type
        with self.assertRaises(ValueError):
            self.validator.load_file('tests/test.txt')

    def test_validate_file(self):
        # Test validating a file that meets the schema and custom rules
        errors = self.validator.validate_file('tests/test.json', {"age": 30})
        self.assertEqual(errors, [])

        # Test validating a file that does not meet the schema
        errors = self.validator.validate_file('tests/invalid.json', {"age": 30})
        self.assertNotEqual(errors, [])

        # Test validating a file that does not meet the custom rules
        errors = self.validator.validate_file('tests/test.json', {"age": 31})
        self.assertNotEqual(errors, [])

if __name__ == '__main__':
    unittest.main()