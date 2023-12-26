from playsound import playsound
import time

CLEAR = "\033[2J\033[H"

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR}{minutes_left:02d}:{seconds_left:02d}", end="\r")
        time.sleep(1)
        time_elapsed += 1

    playsound("alarm.mp3")

minutes = int(input("How many minutes: "))
seconds = int(input("How many seconds: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
