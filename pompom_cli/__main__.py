import time
import sys
from datetime import datetime as dt
from datetime import timedelta
import click
from playsound import playsound
import pandas as pd
import math


@click.command()
@click.argument('ontime', default=25)
@click.argument('breaktime', default=5)
@click.argument('activity', default='Default')
@click.option('--alarm', default='on', help='Alarm sound [on] or [off]')
@click.option('--auto', default='on', help='If [on], timer will automatically loop through each timer cycle. If [off], timer will ask for permission to continue.')
def main(ontime, breaktime, activity, alarm, auto):
    """
    pompom

    A simple program with customizable parameters to fight procrastination and track time.
    """
    while True:
        if auto == 'on':
            timer(activity, ontime, breaktime, alarm)
        elif auto == 'off':
            timer(activity, ontime, breaktime, alarm)
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


def timer(activity, ontime, breaktime, alarm):
    date = dt.now().date().strftime('%Y-%m-%d')
    time_start = dt.now()

    # Timer activated for ontime in seconds.
    click.echo('Timer started! You have {} minutes.'.format(ontime))
    time.sleep(ontime * 60)
    ontime_end = dt.now()
    if alarm == 'on':
        sound_alarm()

    # Break time activated for breaktime in seconds.
    click.echo('Break time! You have {} minutes.'.format(breaktime))
    time.sleep(breaktime * 60)
    breaktime_end = dt.now()
    if alarm == 'on':
        sound_alarm()

    # Use timedeltas to get time_saved and total_time
    # time_saved is the amount of time spent working in minutes
    # total_time is the total timer cycle in minutes
    time_saved = round((ontime_end - time_start).total_seconds() / 60)
    total_time = round((breaktime_end - time_start).total_seconds() / 60)
    tracked_time = {
        'activity': activity.title(),
        'date': date,
        'time_saved': time_saved,
        'total_time': total_time,
    }
    track_time(tracked_time)


# TODO: Add option to change alarm sound
def sound_alarm():
    playsound('./alarm.wav')


# Read activity and time data from tracked_time dictionary and ouptut to times.csv
# times.csv can be read by pomplot.py for data visualization
def track_time(tracked_time):
    times = pd.DataFrame(
        columns=['activity', 'date', 'time_saved', 'total_time'])
    times = times.append(tracked_time, ignore_index=True)
    times.to_csv(path_or_buf='./times.csv', mode='a',
                 header=False, index=False)


if __name__ == '__main__':
    main()
