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
        # REST interface
        "flask >= 2.0.0",
        # AMQP interface
        "pika >= 1.2.0",
        # connection to MySQL
        "mysql-connector-python == 8.0.28",
        # connection to Logstash
        "python-logstash >= 0.4.6",
        # dependency injection
        "dependency_injector >= 4.39.1",
        # Utility to print coloured output in the shell
        "colorama >= 0.4.0",
        # Firebase connection
        'firebase-admin>=5.2.0'
    ],
    python_requires='>=3.9'
)
