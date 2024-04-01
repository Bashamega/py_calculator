from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='calcutils',
    version='0.3',
    packages=find_packages(),
    author='Adam Basha',
    author_email='adam.webtools@gmail.com',
    url='https://github.com/bashamega/py_calculator',
    python_requires='>=3.6',
    description='Utility functions for basic arithmetic calculations',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
