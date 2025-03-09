import unittest
from main import Schema, Validator, ConfigurationFile

class TestMain(unittest.TestCase):
    def test_validator(self):
        schema = Schema('tests/schema.json')
        validator = Validator(schema)
        config_files = [ConfigurationFile(file) for file in ['tests/config1.json', 'tests/config2.yaml']]
        report = validator.validate(config_files)
        self.assertEqual(report['total_files'], 2)
        self.assertEqual(report['files_with_errors'], 0)
        self.assertEqual(report['total_errors'], 0)

if __name__ == '__main__':
    unittest.main()