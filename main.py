# coding:utf-8
'''
import pygame, sys, random, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 300))
screen.fill((255, 255, 255))
dino = pygame.image.load('images/dino1.png')
obs = pygame.image.load('images/obs.png')
dino_squat = pygame.image.load('images/dino_squat.png')
road = pygame.image.load('images/road.png')
obs_x = random.randint(30, 270)
dino_x = 10
dino_y = 200
dino_squat_x = 10
dino_squat_y = 230
status = 0
sky_speed = 0.2
road_long = 1233
road_x = 0
road_y = 280
road_x1 = road_long
jmp_status = False
jmp_speed = 2


def A(B):
    TextFont = pygame.font.SysFont("Fixedsys", 40)
    TF = TextFont.render(B, True, (1, 1, 1))
    return TF


a = A("HI")


def HandleEvent():
    global dino_x, dino_y, dino_squat, status, jmp_speed, jmp_status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                dino_y-=150
                screen.blit(dino, (dino_x, dino_y))
                screen.fill((255, 255, 255))
                pygame.display.update()
            if event.key == K_DOWN:
                status = 1
                pygame.display.update()
        if event.type == KEYUP:
            if event.key == K_SPACE or event.key == K_UP:
                dino_y+=150
                pygame.display.update()
                screen.fill((255, 255, 255))

            if event.key == K_DOWN:
                status = 0
                screen.fill((255, 255, 255))
                pygame.display.update()


def obsscript():
    global obs_x
    obs_tmp = obs_x - 1
    if obs_tmp < dino_x:
        obs_tmp = 700
    pygame.display.update()
    print(obs_tmp)
    screen.blit(obs, (obs_tmp, 230))
    pygame.display.update()


while True:
    screen.fill((255, 255, 255))
    screen.blit(road, (road_x, road_y))
    screen.blit(road, (road_x1, road_y))
    road_x -= sky_speed
    road_x1 -= sky_speed
    if road_x1 <= 0:
        road_x = 0
        road_x1 = road_long
    # obsscript()
    if status == 0:
        screen.blit(dino, (dino_x, dino_y))
    elif status == 1:
        screen.blit(dino_squat, (dino_squat_x, dino_squat_y))
    HandleEvent()
    screen.blit(a, (460, 20))
    pygame.display.update()
'''
import pygame, sys, time, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000, 500))
screen.fill((255, 255, 255))
pygame.display.set_caption("小恐龙")

d1 = pygame.image.load("images/dino1.png")
d2 = pygame.image.load("images/dino_squat.png")
r = pygame.image.load("images/road.png")
e = pygame.image.load("images/obs.png")
gameover = pygame.image.load("images/gameover.png")
dd = pygame.image.load("images/dino_death.png")
retry = pygame.image.load("images/retry.png")
state = 0
sky_speed = 0.5
state_j = False
j_speed = 1
button_x = 0
button_y = 0
reset = 0


def A(B, C, D):
    TextFont = pygame.font.SysFont("simhei", C)
    TF = TextFont.render(B, True, D)
    return TF


class SKY():
    global sky_speed

    def __init__(self):
        self.long = 1233
        self.x = 0
        self.y = 330
        self.x1 = self.long
        self.img = r

    def paint(self):
        screen.blit(self.img, (self.x, self.y))
        screen.blit(self.img, (self.x1, self.y))

    def move(self):
        if state == 3:
            pass
        else:
            self.x -= sky_speed
            self.x1 -= sky_speed
            if self.x1 == 0:
                self.x = 0
                self.x1 = self.long


sky = SKY()


class HERO():
    global state, state_j, j_speed

    def __init__(self):
        self.x1 = 100
        self.y1 = 250
        self.y2 = 280
        self.width = 40
        self.height = 80
        self.img1 = d1
        self.img2 = d2

    def paint(self):
        if state == 0:
            screen.blit(self.img1, (self.x1, self.y1))
        elif state == 1:
            screen.blit(self.img2, (self.x1, self.y2))
        else:
            pass

    def move(self):
        if state == 3:
            pass
        else:
            global state_j, j_speed
            if state_j and self.y1 >= 100:
                self.y1 -= j_speed
                if self.y1 <= 100:
                    state_j = False
            elif state_j == False and self.y1 <= 250:
                self.y1 += j_speed

    def hit(self, c):
        # print(self.x1,self.y1,c.x,c.y)
        return self.x1 >= c.x - self.width and self.x1 <= c.x + c.width and self.y1 >= c.y - self.height and self.y1 <= c.y + c.height


class ENEMY():
    def __init__(self, x):
        self.x = x
        self.y = 300
        self.width = 10
        self.height = 20
        self.img = e

    def paint(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        if state == 3:
            pass
        else:
            self.x -= 0.5


dragon = HERO()


def handleEvent():
    global state, state_j, button_y, button_x, reset
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                state = 1
            elif event.key == K_SPACE and event.key == K_UP:
                #                 print(dragon.y1)
                state_j = True

        elif event.type == KEYUP:
            state = 0
        if event.type == MOUSEMOTION:
            button_x = event.pos[0] - 425 / 2
            button_y = event.pos[1] - 300 / 2
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and state == 3:
            state = 0
            reset = 1
            screen.fill((255, 255, 255))
            pygame.display.update()


def Main():

    global state
    dragon.paint()
    dragon.move()
    sky.paint()
    sky.move()
    synpy()
    for i in es:
        i.paint()
        i.move()
        if checkhit(i) and reset == 0:
            state = 3
            screen.blit(dd, (100, 250))
            screen.blit(gameover, (180, 220))
            screen.blit(retry, (425, 300))
            if reset == 1:
                state = 0
            else:
                screen.fill((255, 255, 255))
                Main()


time = 0
es = []


def synpy():
    global time
    if time == 300:
        time = 0
        es.append(ENEMY(x111))
    time += 1


def checkhit(e1):
    global dragon, state
    if dragon.hit(e1):
        state = 3


while True:
    screen.fill((255, 255, 255))
    Main()
    x111 = random.randint(300, 1000)
    handleEvent()
    pygame.display.update()
