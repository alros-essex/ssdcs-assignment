'''Setup the project'''

from setuptools import setup, find_packages

setup(
    name='adapters',
    version='0.1.0',
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=['pytest', 'pylint'],
    packages=find_packages(include=['generators']),
    test_suite = 'test',
    install_requires=[
        "pika >= 1.2.0"
    ],
    python_requires='>=3.6'
)
