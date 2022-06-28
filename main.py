"""Move mouse

Simple application python. Open program mac and move mouse for specific time.

Author: David Córdoba
Date created: 10/06/2022
Date last modified: 28/06/2022
Python Version: 3.10.5
"""

import datetime
import os
import sys

import pyautogui


def open_app():
    """Open teams application of MAC."""
    os.system('open /Applications/Microsoft\ Teams.app')


def move_mouse(minutes):
    """Main function. move mouse for a determinate time.

    :param minutes: Number of minutes to execute the program move mouse.
    """
    open_app()
    seconds = minutes * 60
    num_loop = 32
    mov_seconds = seconds/(num_loop*2)
    start = datetime.datetime.now()
    print(f"Start time: {start}")
    x = 1200
    y = 100
    for i in range(0, num_loop):
        pyautogui.moveRel(x, y, mov_seconds)
        pyautogui.moveRel(-x, -y, mov_seconds)

    end = datetime.datetime.now()

    elapsed_time = end - start
    print(f"End time: {end}")
    print(f"Duration of sleep: {str(elapsed_time).split('.')[0]}")


if __name__ == '__main__':

    if len(sys.argv) == 2:
        minutes_specified = int(sys.argv[1])
        print(f"Time to execute {minutes_specified}")
        move_mouse(minutes=minutes_specified)
    else:
        default_minutes = 10
        print(f"Time to execute {default_minutes}")
        move_mouse(minutes=default_minutes)


