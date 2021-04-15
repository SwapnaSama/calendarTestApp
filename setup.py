from setuptools import setup, find_packages

setup(
    name='calendar_app_setup',
    version='1.0.0',
    install_requires=[
        'selenium',
        'pytest'
    ],
    packages=find_packages()
)
