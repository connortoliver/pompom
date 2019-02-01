# pompom

pompom is a command line interface (CLI) application that utilizes the pomodoro technique to fight procrastination and help track time.

## Pomodoro technique

The pomodoro technique is a simple technique that helps individuals fight procrastination by using a simple timer.
The standard pomodoro timer is to work for 25 minutes and take a 5 minute break. You can read more about the technique [here](https://en.wikipedia.org/wiki/Pomodoro_Technique "Pomodoro Technique").

## Installation

<!--`pip install pompom`

OR-->

```git clone https://github.com/connortoliver/pompom
cd pompom_cli
pip install -r requirements.txt
python setup.py install
```

## pompom Usage

`pompom [ontime] [breaktime] [activity] [OPTIONS]`

- `ontime` is the amount of time you want to work in minutes. Default is 25 minutes.
- `breaktime` is the amount of break time in minutes per cycle. Default is 5 minutes.
- `activity` is the activity you are working on (studying, reading, programming...). Default is 'Default'.

`pompom 45 15` will create a timer with 45 minutes on, 15 minutes off for activity 'Default'.

`pompom 25 5 Programming` will create a timer with 25 minutes on, 5 minutes off for activity 'Programming'.

## pomplot

<!--Update with pomplot information-->

## pomplot Usage

<!--Update with pomplot usage-->

## How pompom was made

pompom was built using [Click](https://pypi.org/project/click/ "Click on PyPI"), a Python package for creating command line interfaces quickly and easily.