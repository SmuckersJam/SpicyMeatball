import pygame, pgzrun, numpy, math

# Screen Dimension
WIDTH = 800
HEIGHT = 450
anistate = 0
badmen = []
#heroan = []

target = ()

class protag:
    def __init__(self):
        self.Hero = Actor("sus", center =(WIDTH/2,HEIGHT/2))
        self.meatball = Actor("rawball", center = (self.Hero.x,self.Hero.y))
        self.HP = 3
        self.dodgetime = 5
        self.dodge = False
        self.inv = False
        self.invtim = 2
        self.ball = 5
        self.ballready = 1
        self.score = 0
        self.fired = False
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    
    def status(self):
        if self.invtim == 2:
            self.inv = False

    def fire(self):
        if self.fired == True:
            animate(self.meatball, pos=(target))
            if self.meatball.collidepoint(target):
                self.fired = False


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
        numpy.random.randint(-WIDTH, WIDTH*2),
        numpy.random.randint(-HEIGHT,HEIGHT*2)
    )

def player_move():
    global Hero
    if Hero.dodge == False:
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
        if Hero.dodgetime == 5:
            if Hero.down == True or Hero.left == True or Hero.up == True or Hero.right == True:
                if keyboard.lshift: 
                    Hero.dodge = True


def dodge():
    global anistate
    if Hero.dodge == True:
        Hero.inv = True
        if Hero.left == True and Hero.Hero.x > 19:
            Hero.Hero.x -= 5
        if Hero.right == True and Hero.Hero.x < WIDTH-10:
            Hero.Hero.x += 5
        if Hero.up == True and Hero.Hero.y > 10:
            Hero.Hero.y -= 5
        if Hero.down == True and Hero.Hero.y < HEIGHT-10:
            Hero.Hero.y += 5
        anistate += 1
        if anistate == 30:
            Hero.inv = False
            Hero.dodgetime = 0
            Hero.dodge = False
    else:
        anistate = 0

def tim_stuff():
    global Hero
    if Hero.dodgetime < 5:
        Hero.dodgetime += 1
    if Hero.invtim < 2:
        Hero.invtim += 1
    
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
        if x.carrot.collidepoint(Hero.Hero.x, Hero.Hero.y):
            if Hero.inv == False:
                Hero.HP -= 1
                Hero.invtim = 0
                Hero.inv = True

clock.schedule_interval(tim_stuff, 1.0)

def draw():
    screen.fill((0,0,0))
    if Hero.HP > 0:
        Hero.Hero.draw()
        for x in badmen:
            x.carrot.draw()    
        if Hero.fired == True:
            Hero.meatball.draw()
        screen.draw.text(str(Hero.dodgetime), center=(10,10), fontsize=32)
        screen.draw.text(str(Hero.HP), center=(25,10), fontsize=32)
        screen.draw.text(str(Hero.invtim), center=(40,10), fontsize=32)
    else:
        screen.draw.text("lol", center=(WIDTH/2, HEIGHT/2), fontsize=80)

def update():
    if Hero.HP > 0:
        update_sus()
        player_move()
        dodge()
        ouch()
        Hero.status()
        Hero.fire()

def on_mouse_down(pos):
    global target
    if Hero.dodge == False:
        if Hero.fired == False:
            if Hero.ballready == 1:
                Hero.meatball.center = (Hero.Hero.x,Hero.Hero.y)
                target = (pos[0],pos[1])
                Hero.ball -= 1
                Hero.ballready = 0
                Hero.fired = True

pgzrun.go()

