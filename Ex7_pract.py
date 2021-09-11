# from pygame import mixer
# mixer.init()
#
# mixer.music.load("Final Intro (6 seconds).mp3")
# mixer.music.set_volume(0.7)
#
# if True:
#     mixer.music.play()


# mixer.init()
# mixer.music.load("Final Intro (6 seconds).mp3")
# mixer.music.set_volume(0.7)
# mixer.music.play()
# print("hello")


import pygame
file = 'Final Intro (6 seconds).mp3'
pygame.init()
pygame.mixer.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.event.wait()




