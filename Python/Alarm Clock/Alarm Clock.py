import time
from playsound import playsound

def Alarm(seconds):
    while seconds > 0:
        seconds -= 1
        time.sleep(1)

        seconds_left = seconds % 60
        minutes_left = seconds // 60

        print(f"\r{minutes_left:02d}:{seconds_left:02d}", end="")

    playsound('alarm.mp3')


all_seconds = int(input("How many seconds to wait? "))
Alarm(all_seconds)
