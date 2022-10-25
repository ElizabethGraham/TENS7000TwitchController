# GPIO 23
import RPi.GPIO as GPIO
import pygame, sys
from pygame.locals import *
import time

GPIO.setwarnings(False)
# GPIO numbers instead of board numbers
GPIO.setmode(GPIO.BCM)
# GPIO Set Output Mode
GPIO.setup(23, GPIO.OUT)
# LOW PIN AKA CANCEL SHOCK
GPIO.output(23, GPIO.LOW)

pygame.init()
BLACK = (0, 0, 0)
WIDTH = 100
HEIGHT = 100
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
windowSurface.fill(BLACK)
trigger_key = pygame.K_g

x = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            key = event.key
            if key == trigger_key:
                if x == 0:
                    print('Shock triggered...')
                    GPIO.output(23, GPIO.HIGH) # Shock
                    time.sleep(1)
                    GPIO.output(23, GPIO.LOW) # Cancel shock
