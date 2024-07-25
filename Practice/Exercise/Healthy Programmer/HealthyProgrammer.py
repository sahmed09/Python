from pygame import mixer
from datetime import datetime
from time import time


def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # music_on_loop("Tera.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exercisesecs = 5
    eyessecs = 5

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'drank' to stop the alarm.")
            music_on_loop("Tera.mp3", "drank")
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye Exercise Time. Enter 'done eyes' to stop the alarm.")
            music_on_loop("Afreen Afreen.mp3", "done eyes")
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exercisesecs:
            print("Physical Activity Time. Enter 'done phy' to stop the alarm.")
            music_on_loop("Tu_Hi_Tu.mp3", "done phy")
            init_exercise = time()
            log_now("Physical Activity done at")
