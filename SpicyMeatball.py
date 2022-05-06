import pygame, pgzrun, numpy, math

# Screen Dimension
WIDTH = 960
HEIGHT = 672
anistate = 0
badmen = []
#heroan = []

target = ()
tarx = 0.0
tary = 0.0
mousex = 0.0
mousey = 0.0

class protag:
    def __init__(self):
        self.Hero = Actor("rammynuggy", center=(WIDTH/2,HEIGHT/2))
        self.meatball = Actor("rawball", center = (self.Hero.x,self.Hero.y))
        self.HP = 3
        self.dodgetime = 5
        self.dodge = False
        self.inv = False
        self.invtim = 2
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
            if self.meatball.x > WIDTH or self.meatball.x < 0 or self.meatball.y < 0 or self.meatball.y > HEIGHT or self.meatball.x == mousex or self.meatball.y == mousey:
                self.fired = False
                self.meatball.center = (self.Hero.x,self.Hero.y)


class carot:
    def __init__ (self):
        self.carrot = Actor("sus", center=(0,0))
        self.HP = 1
        self.respawn = 0

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
        if keyboard.w and Hero.Hero.y > 3:
            Hero.Hero.y -= 3
            Hero.up = True
        else:
            Hero.up = False
        if keyboard.a and Hero.Hero.x > 0:
            Hero.Hero.x -= 3
            Hero.left = True
            Hero.Hero.image = ("lrammynuggy")
        else:
            Hero.left = False
        if keyboard.d and Hero.Hero.x < WIDTH-72:
            Hero.Hero.x += 3
            Hero.right = True
            Hero.Hero.image = ("rammynuggy") 
        else:
            Hero.right = False
        if keyboard.s and Hero.Hero.y < HEIGHT-88:
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
        if anistate == 0:
            if Hero.right == True:
                Hero.Hero.image = ("rammyroll1")
            if Hero.left == True:
                Hero.Hero.image = ("'rammyroll1")
        if anistate == 10:
            if Hero.right == True:
                Hero.Hero.image = ("rammyroll2")
            if Hero.left == True:
                Hero.Hero.image = ("lrammyroll2")
        if anistate == 20:
            if Hero.right == True:
                Hero.Hero.image = ("rammyroll3")
            if Hero.left == True:
                Hero.Hero.image = ("lrammyroll3")
        if anistate == 30:
            if Hero.right == True:
                Hero.Hero.image = ("rammynuggy")
            if Hero.left == True:
                Hero.Hero.image = ("lrammynuggy")
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
    if Hero.ballready < 1:
        Hero.ballready += 1
    for x in badmen:
        if x.HP == 0:
            x.respawn += 1
    
def update_sus():
    global Hero
    for x in badmen:
        if x.HP > 0:
            if x.carrot.x < Hero.Hero.x:
                x.carrot.x += 0.5
            if x.carrot.x > Hero.Hero.x:
                x.carrot.x -= 0.5
            if x.carrot.y < Hero.Hero.y:
                x.carrot.y += 0.5
            if x.carrot.y > Hero.Hero.y:
                x.carrot.y -= 0.5
        if x.respawn == 2:
            x.respawn = 0
            x.carrot.image = ("sus")
            x.HP += 1
            x.carrot.pos = (
                numpy.random.randint(-WIDTH, WIDTH*2),
                numpy.random.randint(-HEIGHT,HEIGHT*2)
            )


def susdeath():
    global Hero
    for x in badmen:
        if x.HP > 0:
            if Hero.meatball.colliderect(x.carrot):
                Hero.score += 1
                x.HP -= 1
                x.carrot.image = ("deadcarrot")

def ouch():
    global Hero, badmen
    for x in badmen:
        if x.HP > 0:
            if x.carrot.collidepoint(Hero.Hero.x, Hero.Hero.y):
                if Hero.inv == False:
                    Hero.HP -= 1
                    Hero.invtim = 0
                    Hero.inv = True

clock.schedule_interval(tim_stuff, 1.0)

def draw():
    screen.blit("foodroom", (0,0))
    if Hero.HP > 0:
        Hero.Hero.draw()
        for x in badmen:
            x.carrot.draw()    
        if Hero.fired == True:
            Hero.meatball.draw()
        screen.draw.text("Health: " + str(Hero.HP), topleft=(10,10), fontsize=32)
        screen.draw.text("Score: " + str(Hero.score), topleft=(HEIGHT-10,10), fontsize=32)
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
        susdeath()

def on_mouse_down(pos):
    global target, tarx, tary, Hero, mousex, mousey
    if Hero.dodge == False:
        if Hero.fired == False:
            if Hero.ballready == 1:
                mousex = pos[0]
                mousey = pos[1]
                distx = Hero.Hero.x - mousex
                disty = Hero.Hero.y - mousey
                if Hero.Hero.y > mousey:
                    bigy = Hero.Hero.y
                    bigx = Hero.Hero.x
                    smally = mousey
                    smallx = mousex
                else:
                    bigy = mousey
                    bigx = mousex
                    smally = Hero.Hero.y
                    smallx = Hero.Hero.x
                slope = ((Hero.Hero.y - disty) / (Hero.Hero.x - distx))
                Hero.fired = True
                Hero.ballready = 0
                Hero.meatball.center = (Hero.Hero.x,Hero.Hero.y)
                tary = (slope*distx) + Hero.Hero.y
                tarx = ((disty - Hero.Hero.y) / slope) + Hero.Hero.x
#                if Hero.Hero.x < pos[0]:
#                    tarx = (pos[1] - Hero.Hero.y) / slope
#                if Hero.Hero.x > pos[0]:
#                    tarx = -((pos[1] - Hero.Hero.y)/slope)
#                if Hero.Hero.x < pos[1]:
#                    tary = (slope*pos[0]) + Hero.Hero.y
#                if Hero.Hero.y > pos[1]:
#                    tary = -((slope*pos[0]) + Hero.Hero.y)
                target = (tarx,tary)

pgzrun.go()

