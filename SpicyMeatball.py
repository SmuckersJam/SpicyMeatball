import pygame, pgzrun, numpy, math

# Screen Dimension
WIDTH = 600
HEIGHT = 600

badmen = []

class protag:
    Hero = Actor("sus", center =(WIDTH/2,HEIGHT/2))
    #meatball = Actor("meatball", center = (self.Hero.x,self.Hero.y))
    HP = 3
    dodgetime = 5
    inv = False
    ball = 5
    score = 0
    fired = False
    left = False
    right = False
    up = False
    down = False


    def fire(self):
        pass

class carot:
    def __init__ (self):
        self.carrot = Actor("sus", center=(0,0))
        self.HP = 1
        self.respawn = 0

    def death(self):
        pass

Hero = protag()

# Initializes the badmen
for x in range(25):
    badmen.append(carot())

for x in badmen:
    x.carrot.pos = (
        numpy.random.randint(0, WIDTH),
        numpy.random.randint(0,HEIGHT)
    )

def player_move():
    global Hero
    if keyboard.w and Hero.Hero.y > 64:
        Hero.Hero.y -= 3
        Hero.up = True
    else:
        Hero.up = False
    if keyboard.a and Hero.Hero.x > 64:
        Hero.Hero.x -= 3
        Hero.left = True
    else:
        Hero.left = False
    if keyboard.d and Hero.Hero.x < WIDTH-64:
        Hero.Hero.x += 3
        Hero.right = True
    else:
        Hero.right = False
    if keyboard.s and Hero.Hero.y < HEIGHT-64:
        Hero.Hero.y += 3
        Hero.down = True
    else:
        Hero.down = False
    if keyboard.lshift:
        dodge()

def dodge():
    pass
    
def update_sus():
    global Hero
    for x in badmen:
        if x.carrot.x < Hero.Hero.x:
            x.carrot.x += 0.5
        if x.carrot.x > Hero.Hero.x:
            x.carrot.x -= 0.5
        if x.carrot.y < Hero.Hero.y:
            x.carrot.y += 0.5
        if x.carrot.y > Hero.Hero.y:
            x.carrot.y -= 0.5

def ouch():
    global Hero, badmen
    for x in badmen:
        if x.badmen.collidepoint(Hero.Hero.x, Hero.Hero.y):
            if Hero.inv == False:
                Hero.HP -= 1
                Hero.inv = True

def draw():
    screen.fill((0,0,0))
    Hero.Hero.draw()
    for x in badmen:
        x.carrot.draw()

def update():
    update_sus()
    player_move()

pgzrun.go()

