from setuptools import setup

setup(
    name='pompom',
    version='0.1.0',
    packages=['pompom'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pompom=pompom.__main__:main
    ''',
)
