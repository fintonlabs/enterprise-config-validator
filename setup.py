from setuptools import setup, find_packages

setup(
    name='ConfigValidator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'jsonschema==3.2.0',
        'PyYAML==5.4.1',
    ],
    entry_points={
        'console_scripts': [
            'configvalidator=configvalidator:main',
        ],
    },
)