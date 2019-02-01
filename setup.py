import setuptools

setuptools.setup(
    name='pompom',
    version='0.1.0',
    description='A simple pomodoro timer and time tracker',
    url='https://github.com/connortoliver/pompom',
    packages=setuptools.find_packages(),
    install_requires=[
        'click>=7.0',
    ],
    entry_points='''
        [console_scripts]
        pompom=pompom.__main__:main
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
