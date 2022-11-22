import pygame
from ant import Ant
import random
from state import *
from ant_states import *
from antfarm_states import *

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 80, 40
SCALE = 17

display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()

# State Machine of Ant

home = Home()
search = Search()
c_f = CarringFood()
c_w = CarringWater()
gh = GoingHome()

ant_states = [home,search,c_f,c_w,gh]
ant_trans = {
    "post_spawn" : Transition(home, search),
    "found_watter" : Transition(search, c_w),
    "found_food" : Transition(search, c_f),
    "gh1" : Transition(c_w, gh),
    "gh2" : Transition(c_f, gh),
    "home" : Transition(gh, home)
}

ant_fsm = FSM(ant_states,ant_trans)

# State Machine of Ant Farm

empty = Empty()
h_f = HasFood()
h_w = HasWater()
sp = Spawn()

antfarm_states = [empty,h_f,h_w,sp]
antfarm_trans = {
    "add_food": Transition(empty, h_f),
    "add_watter": Transition(empty, h_w),
    "spawn_food": Transition(h_f, sp),
    "spawn_watter": Transition(h_w, sp),
    "spawn": Transition(sp, empty)
}

farm_fsm = FSM(antfarm_states, antfarm_trans)

# Ant

ant = Ant()

GAME_EVENT = pygame.event.custom_type()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == GAME_EVENT:
            print(event.txt)

    display.fill("white")

    d = (round(random.choice([-1,0,1])),round(random.choice([-1,0,1])))

    ant.move(d)

    ant.draw(display)

    # update window
    pygame.display.flip()
    clock.tick(15)

pygame.quit()


    