from setuptools import setup, find_packages

setup(
    name='safe_repository',
    version='0.1.0',
    packages=find_packages(include=['safe_repository']),
    test_suite = 'test',
    install_requires=[
        "flask >= 2.0.0",
        "pika >= 1.2.0",
        "mysql-connector-python == 8.0.28"

    ],
    python_requires='>=3.6'
)
