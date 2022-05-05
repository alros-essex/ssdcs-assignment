'''Setup the project'''

from setuptools import setup, find_packages

setup(
    name='my_monit',
    version='0.1.0',
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=['pytest', 'pylint'],
    packages=find_packages(include=['my_monit']),
    test_suite = 'test',
    install_requires=[
        "flask >= 2.0.0",
        "pika >= 1.2.0",
        "mysql-connector-python == 8.0.28",
        "python-logstash >= 0.4.6",
        "dependency_injector >= 4.39.1",
        "pyjwt >= 2.3.0",
        "colorama >= 0.4.0",
        'firebase-admin>=5.2.0'
    ],
    python_requires='>=3.9'
)
