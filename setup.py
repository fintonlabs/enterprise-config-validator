from setuptools import setup, find_packages

setup(
    name='config-validator',
    version='0.1.0',
    description='A Python application to validate JSON and YAML configuration files.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'jsonschema==3.2.0',
        'pyyaml==5.4.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)