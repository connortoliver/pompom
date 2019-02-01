from setuptools import setup

setup(
    name='pompom',
    version='0.1',
    py_modules=['pompom'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pompom=pompom:timer
    ''',
)
