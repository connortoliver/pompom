import time
import sys
import click
from playsound import playsound


@click.command()
@click.argument('ontime', default=25)
@click.argument('breaktime', default=5)
@click.argument('activity', default='Default')
@click.option('--alarm', default='on', help='Alarm sound [on] or [off]')
@click.option('--auto', default='on', help='If [on], timer will automatically loop through each timer session. If [off], timer will ask for permission to continue.')
def main(ontime, breaktime, activity, alarm, auto):
    """
    pompom

    A simple program with customizable parameters to fight procrastination and track time.
    """
    while True:
        if auto == 'on':
            timer(ontime, breaktime, alarm)
        elif auto == 'off':
            timer(ontime, breaktime, alarm)
            click.echo('Continue? [Y/N] ')
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


def timer(ontime, breaktime, alarm):
    # Variables created because time.sleep() function requires argument to be in seconds.
    ontime_secs = ontime * 60
    breaktime_secs = breaktime * 60

    click.echo('Timer started! You have {} minutes.'.format(ontime))
    time.sleep(ontime_secs)

    click.echo('Break time! You have {} minutes.'.format(breaktime))
    if alarm == 'on':
        sound_alarm()

    time.sleep(breaktime_secs)

    if alarm == 'on':
        sound_alarm()


def sound_alarm():
    playsound('./alarm.wav')


if __name__ == '__main__':
    main()
