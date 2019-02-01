import time
import sys
import click


@click.command()
@click.option('--ontime', default=25,           help='Amount of time in minutes spent doing something per timer session.')
@click.option('--breaktime', default=5,         help='Amount of break time in minutes per timer session.')
@click.option('--activity', default='Default',  help='Activity you\'re doing (e.g. studying, reading, programming)')
@click.option('--sound', default='on',          help='Alarm sound [on] or [off]')
@click.option('--auto', default='on',           help='If [on], timer will automatically loop through each timer session. If [off], timer will ask for permission to continue.')
def timer(ontime, breaktime, activity, sound, auto):
    """
    pompom

    A simple program with customizable parameters to fight procrastination and track time.
    """
    # Variables created because time.sleep() function requires argument to be in seconds.
    ontime_secs = ontime * 60
    breaktime_secs = breaktime * 60

    if auto == 'on':
        while True:
            click.echo('Timer started! You have {} minutes.'.format(ontime))
            time.sleep(ontime_secs)

            click.echo('Break time! You have {} minutes.'.format(breaktime))
            time.sleep(breaktime_secs)
    elif auto == 'off':
        while True:
            click.echo('Timer started! You have {} minutes.'.format(ontime))
            time.sleep(ontime_secs)

            click.echo('Break time! You have {} minutes.'.format(breaktime))
            time.sleep(breaktime_secs)

            click.echo('Continue? [Y/N] ', nl=False)
            restart = click.getchar()

            if restart == 'Y' or restart == 'y':
                continue
            elif restart == 'N' or restart == 'n':
                break
            else:
                click.echo('Please enter \'Y\' or \'N\'.')
                break
    else:
        click.echo('Please type \'on\' or \'off\' for --auto option.')


if __name__ == '__main__':
    timer()
