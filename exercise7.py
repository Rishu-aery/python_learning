# Healthy programmer

# Water - Water.mp3  (3.5 litres)-log
# Eyes - eyes .mp3  (30 minutes)- log
# Physical activity - physical.mp3  (45 minutes)-log


from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
        elif a=='q':
            exit()

def log_now(msg):
    with open('my_logs.txt','a')as f:
        f.write(f"{msg},{datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("Final Intro (6 seconds).mp3",'stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_time=10
    eyes_time = 20
    exercise_time = 30
    while True:
        if time()-init_water > water_time:
            print('Water drinkin Time... Write "done" if you drink water or "q" to quit')
            musiconloop('CuteHappy Short Audios For Edits!.mp3','done')
            init_water = time()
            log_now("Water drinking at:")

        if time() - init_eyes > eyes_time:
            print('Eyes exercise Time... Write "done" if you complete your eye exercise or "q" to quit')
            musiconloop('CuteHappy Short Audios For Edits!.mp3', 'done')
            init_eyes = time()
            log_now("Eye exercise done at:")

        if time() - init_exercise > exercise_time:
            print('Exercise Time... Write "done" if you complete your exercise or "q" to quit')
            musiconloop('CuteHappy Short Audios For Edits!.mp3', 'done')
            init_exercise = time()
            log_now("Exercise done at:")



