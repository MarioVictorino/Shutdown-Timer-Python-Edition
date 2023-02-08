# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

import keyboard as keyboard

print('Enter time to shutdown in seconds or press q to quit')
print('1 Hour = 3600 | 2 Hours = 7200 | 3 Hours 10800 | 4 Hours = 14400')

keepRunning = True

while keepRunning:
    time = input()
    if time.isnumeric():
        x = int(time)
        if (x >= 0) and (x <= 28800):
            output = ("shutdown /s /t " + time)
            os.system(output)
    elif not (time.isnumeric()):
        if time == 'q':
            sys.exit()
        else:
            print("Invalid Submission")
