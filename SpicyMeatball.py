import pygame, pgzrun, numpy, math

# Screen Dimension
WIDTH = 600
HEIGHT = 600

class protag:
    Hero = Actor("carrot.png", pos =(WIDTH/2,HEIGHT/2))
    HP = 3
    dodgetime = 5
    ball = 5
    score = 0
    fired = False

    def fire(self):
        pass

class Carot:
    carrot = Actor("carrot.png", pos=(10,10))
    HP = 1
    respawn = 0

    def death(self):
        pass

Hero = protag()

def Draw():
    background = "black"
    Hero.Hero.draw()

