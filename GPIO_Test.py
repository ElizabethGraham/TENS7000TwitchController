# GPIO 23
import RPi.GPIO as GPIO
import pygame, sys
from pygame.locals import *
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPION Numbers instead of board numbers.
GPIO.setup(23, GPIO.OUT) # GPIO Set Output Mode
GPIO.output(23, GPIO.LOW) # LOW PIN AKA CANCEL SHOCK
pygame.init()
BLACK = (0, 0, 0)
WIDTH = 100
HEIGHT = 100
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
windowSurface.fill(BLACK)

x = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            key = event.key
            if key == pygame.K_g:
                if x == 0:     
                    print('you sadistic fuck')
                    GPIO.output(23, GPIO.HIGH) # HIGH PIN AKA Shock Pin
                    time.sleep(1)
                    GPIO.output(23, GPIO.LOW) # LOW PIN AKA CANCEL SHOCK