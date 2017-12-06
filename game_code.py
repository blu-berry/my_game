import pygame
import math
import pickle


# *****************************************************************************************************
# *****************************************************************************************************

# display resolution
width = 1024
height = 768

# fonts used

pygame.font.init()

my_font = pygame.font.SysFont("Arial", 22)
about_text = my_font.render("This is the description of the game, developers and other stuff like that...", False, (255, 255, 255))

# display, files and FPS setup
pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Display")
clock = pygame.time.Clock()
victoryImg = pygame.image.load("win.png")
menuImg = pygame.image.load("menu.png")

exit = False
about = True


# starting position of player
sprite_x = 512
sprite_y = 758

# *****************************************************************************************************
# *****************************************************************************************************

# main menu
width_values_list = [365, 340, 211, 142]
picker_y_chords_list = [180, 305, 427, 552]
picker_x_chords_list = [330, 345, 400, 430]
picker_pos = 0
picker_height = 55


def main_menu(events):
    global picker_pos
    global map_num
    global exit
    global about
    global about_text
    global sprite_x
    global sprite_y
    picker_x = picker_x_chords_list[picker_pos]
    picker_y = picker_y_chords_list[picker_pos]
    picker_width = width_values_list[picker_pos]
    gameDisplay.fill((42, 44, 48))
    gameDisplay.blit(menuImg, (312, 84))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (picker_x, picker_y, picker_width, picker_height), 2)
    for event in events:
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            picker_pos -= 1
            if picker_pos < 0:
                picker_pos = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            picker_pos += 1
            if picker_pos > 3:
                picker_pos = 3
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            if picker_pos == 0:
                map_num += 1
                sprite_x = 512
                sprite_y = 758
            if picker_pos == 1:
                sprite_x = 512
                sprite_y = 758
                map_num = pickle.load(open("save.p", "rb"))
                return map_num
            if picker_pos == 2:
                map_num = len(maps_list) - 2
            if picker_pos == 3:
                exit = True


# *****************************************************************************************************
# *****************************************************************************************************

def about_screen(events):
    global about_text
    global map_num
    gameDisplay.fill((42, 44, 48))
    gameDisplay.blit(about_text, (100, 100))
    for event in events:
        if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
            map_num = 0


# *****************************************************************************************************
# *****************************************************************************************************


# basic level
def level_1(events):
    global sprite_x
    global sprite_y
    global map_num
    global maps_list
    gameDisplay.fill((42, 44, 48))
    pygame.draw.rect(gameDisplay, (255, 255, 255), (492, 0, 40, 40), 3)
    pygame.draw.circle(gameDisplay, (40, 119, 252), (sprite_x, sprite_y), 10, 5)
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[0], y_axis_level_1[0]), 2, 0)
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[1], y_axis_level_1[1]), 2, 0)
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[2], y_axis_level_1[2]), 2, 0)
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[3], y_axis_level_1[3]), 2, 0)
    for event in events:
        if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
            map_num = 0
            sprite_x = 512
            sprite_y = 758

    # bullets logic for level 1
    # bullet1
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[0], y_axis_level_1[0]), 2, 0)
    x_axis_level_1[0] -= 5
    if x_axis_level_1[0] < 0:
        x_axis_level_1[0] = width

    # bullet2
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[1], y_axis_level_1[1]), 2, 0)
    x_axis_level_1[1] += 7
    if x_axis_level_1[1] > width:
        x_axis_level_1[1] = 0

    # bullet3
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[2], y_axis_level_1[2]), 2, 0)
    x_axis_level_1[2] += 1
    if x_axis_level_1[2] > width:
        x_axis_level_1[2] = 0

    # bullet4
    pygame.draw.circle(gameDisplay, (255, 255, 255), (x_axis_level_1[3], y_axis_level_1[3]), 2, 0)
    x_axis_level_1[3] -= 3
    if x_axis_level_1[3] < 0:
        x_axis_level_1[3] = width

    if (math.sqrt(((sprite_x - x_axis_level_1[0]) ** 2) + ((sprite_y - y_axis_level_1[0]) ** 2))) < 12:
        sprite_x = 512
        sprite_y = 758
    if (math.sqrt(((sprite_x - x_axis_level_1[1]) ** 2) + ((sprite_y - y_axis_level_1[1]) ** 2))) < 12:
        sprite_x = 512
        sprite_y = 758
    if (math.sqrt(((sprite_x - x_axis_level_1[2]) ** 2) + ((sprite_y - y_axis_level_1[2]) ** 2))) < 12:
        sprite_x = 512
        sprite_y = 758
    if (math.sqrt(((sprite_x - x_axis_level_1[3]) ** 2) + ((sprite_y - y_axis_level_1[3]) ** 2))) < 12:
        sprite_x = 512
        sprite_y = 758

    if sprite_y < 40:
        if sprite_x < 532 and sprite_x > 492:
            if map_num < (len(maps_list) - 3):
                map_num += 1
            else:
                map_num = (len(maps_list) - 1)
            sprite_x = 512
            sprite_y = 758


# *****************************************************************************************************
# *****************************************************************************************************

# victory screen
def win(events):
    global map_num
    gameDisplay.fill((42, 44, 48))
    gameDisplay.blit(victoryImg, (362, 134))
    for event in events:
        if event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
            map_num = 0


# maps list and map counter
maps_list = [main_menu, level_1, about_screen, win]
map_num = 0


# *****************************************************************************************************
# *****************************************************************************************************

# save and load system
load_times = 0

def save_progress(map_position):
    if map_num > 0 and map_num < (len(maps_list) - 2):
        pickle.dump(map_position, open("save.p", "wb"))


def load_progress():
        map_num = pickle.load(open("save.p", "rb"))
        return map_num
        print(map_num)


# *****************************************************************************************************
# *****************************************************************************************************

# bullet starting positions
bullet1_x = 1024
bullet1_y = 512
bullet2_x = 0
bullet2_y = 128
bullet3_x = 0
bullet3_y = 256
bullet4_x = 1024
bullet4_y = 700

# bullet positions lists
x_axis_level_1 = [bullet1_x, bullet2_x, bullet3_x, bullet4_x]
y_axis_level_1 = [bullet1_y, bullet2_y, bullet3_y, bullet4_y]


pygame.key.set_repeat(10, 10)

# *****************************************************************************************************
# *****************************************************************************************************

while not exit:

    events = list(pygame.event.get())

    for event in events:
        if event.type == pygame.QUIT:
            exit = True

        # save logic
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            if map_num > 0 and map_num < (len(maps_list) - 2):
                save_progress(map_num)

        # movement logic
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            sprite_x -= 2
            maps_list[map_num](events)
            if sprite_x < 10:
                sprite_x = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            sprite_x += 2
            maps_list[map_num](events)
            if sprite_x > (width - 10):
                sprite_x = (width - 10)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            sprite_y -= 2
            maps_list[map_num](events)
            if sprite_y < 10:
                sprite_y = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            sprite_y += 2
            maps_list[map_num](events)
            if sprite_y > (height - 10):
                sprite_y = (height - 10)

    # map change logic
    maps_list[map_num](events)


    # display update and FPS
    pygame.display.update()
    clock.tick(500)

pygame.quit()
quit()

