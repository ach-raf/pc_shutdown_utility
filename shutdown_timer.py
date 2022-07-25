import os
import time


def shutdown():
    print('Shutting down ...')
    os.system('shutdown -s')


def countdown(_time_in_seconds):
    while _time_in_seconds:
        minutes, seconds = divmod(_time_in_seconds, 60)
        # 02d formats an integer (d) to a field of minimum width 2 (2), with zero-padding on the left (leading 0):
        time_format = f'{minutes:02d}:{seconds:02d}'
        print(time_format, end='\r')
        time.sleep(1)
        _time_in_seconds -= 1


def main():
    user_input = input('Write the time in minutes to shutdown the computer : ')
    time_in_seconds = int(user_input) * 60
    countdown(time_in_seconds)
    shutdown()


if __name__ == '__main__':
    main()
