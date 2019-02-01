import setuptools

setuptools.setup(
    name='pompom',
    version='0.1.0',
    description='A CLI pomodoro timer and time tracker',
    url='https://github.com/connortoliver/pompom',
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
        'playsound',
    ],
    entry_points={
        'console_scripts': [
            'pompom=pompom_cli.__main__:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
