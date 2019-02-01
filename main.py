#! python3.7
import time
import sys
import click


@click.command()
@click.option('--ontime', default=25,           help='Amount of time in minutes spent doing something per timer session.')
@click.option('--breaktime', default=5,         help='Amount of break time in minutes per timer session.')
@click.option('--activity', default='Default',  help='Activity you\'re doing (e.g. studying, reading, programming)')
@click.option('--sound', default=True,          help='Alarm sound [on] or [off]')
@click.option('--auto', default=True,           help='If [on], timer will automatically loop through each timer session. If [off], timer will ask for permission to continue.')
def timer(ontime, breaktime, activity, sound, auto):
    """
    pompom-cli

    A simple program with customizable parameters to fight procrastination and track time.

    Usage: python main.py [--ontime int] [--breaktime int] [--activity str] [--sound bool] [--auto bool]
    """
    # Variables created because time.sleep() function requires argument to be in seconds.
    ontime_secs = ontime * 60
    breaktime_secs = breaktime * 60

    if auto == 'on':
        while True:
            print('Timer started! You have {} minutes.'.format(ontime))
            time.sleep(ontime_secs)

            print('Break time! You have {} minutes.'.format(breaktime))
            time.sleep(breaktime_secs)
    elif auto == 'off':
        while True:
            print('Timer started! You have {} minutes.'.format(ontime))
            time.sleep(ontime_secs)

            print('Break time! You have {} minutes.'.format(breaktime))
            time.sleep(breaktime_secs)

            restart = input('Restart? (Y/N): ')
            if restart == 'Y' or restart == 'y':
                continue
            elif restart == 'N' or restart == 'n':
                break
            else:
                print('Please enter \'Y\' or \'N\'.')
    else:
        print('Please type \'on\' or \'off\' for --auto option.')


if __name__ == '__main__':
    timer()
