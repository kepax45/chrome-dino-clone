import pygame
import random
import pickle
import os
from classes import *

dino_sprite = pygame.image.load(os.path.join('..', 'src', 'dino-sprite.png'))
screen_width = 1400
screen_height = 400
def get_sprite(image, x, y, width, height):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(image, (0, 0), (x, y, width, height))
    return sprite
def get_mouse():
    return pygame.mouse.get_pos()
def write_highscore(score):
    out_file = open('score.dat', 'wb')
    pickle.dump(score, out_file)
    out_file.close()
def get_highscore():
    in_file = open('score.dat', 'rb')
    data = pickle.load(in_file)
    in_file.close()
    return int(data)
def get_score_width(score):
    width = 0
    for i in range(len(score)):
        digit = int(score[i])
        width += numbers[digit].get_width()+4+2*(digit==1)
    return width
zero_sprite = get_sprite(dino_sprite, 953, 1, 19, 22)
one_sprite = get_sprite(dino_sprite, 975, 1, 17, 22)
two_sprite = get_sprite(dino_sprite, 993, 1, 19, 22)
three_sprite = get_sprite(dino_sprite, 1013, 1, 19, 22)
four_sprite = get_sprite(dino_sprite, 1033, 1, 19, 22)
five_sprite = get_sprite(dino_sprite, 1053, 1, 19, 22)
six_sprite = get_sprite(dino_sprite, 1073, 1, 19, 22)
seven_sprite = get_sprite(dino_sprite, 1093, 1, 19, 22)
eight_sprite = get_sprite(dino_sprite, 1113, 1, 19, 22)
nine_sprite = get_sprite(dino_sprite, 1133, 1, 19, 22)
game_over_sprite = get_sprite(dino_sprite, 953, 28, 382, 22)
numbers = [zero_sprite, one_sprite, two_sprite, three_sprite, four_sprite, five_sprite, six_sprite, seven_sprite, eight_sprite, nine_sprite]
hi_sprite = get_sprite(dino_sprite, 1153, 1, 39, 22)
def get_random_obstacle():
    image = obstacles[random.randint(0, len(obstacles)-1)]
    o = Object(1450, 400-image.get_height(), 0, 0)
    o.force_image(image)
    o.adjust_transform()
    return o
def make_score(score):
    score = format_score(score)
    res = pygame.Surface((get_score_width(score), 300), pygame.SRCALPHA)
    x = 0
    for i in range(len(score)):
        digit = int(score[i])
        res.blit(numbers[digit], (x+int(digit==1), 0))
        x += numbers[digit].get_width()+4+2*(digit==1)
    #res.blit(hi_sprite, (x, 0))
    return res
def make_highscore():
    res = pygame.Surface((get_score_width(format_score(get_highscore()))+hi_sprite.get_width()*1.5, 300), pygame.SRCALPHA)
    res.blit(hi_sprite, (0, 0))
    res.blit(make_score(get_highscore()), (hi_sprite.get_width()*1.5, 0))
    res.set_alpha(128)
    return res
def center_x(width):
    return width/2
def center_y(height):
    return height/2
def format_score(score):
    score = str(score)
    return '0'*(5-len(score))+score
score_display = Object(screen_width-get_score_width(format_score(0)), 0, 0, 0)
score_display.force_image(make_score('0'))
highscore_display = Object(1000, 0, 0, 0)
highscore_display.force_image(make_highscore())
restart_button_sprite = get_sprite(dino_sprite, 1, 1, 72, 64)
restart_button = Object(center_x(screen_width)-restart_button_sprite.get_width()/2, center_y(screen_height)-restart_button_sprite.get_height()/2, 100, 100)
restart_button.force_image(restart_button_sprite)
game_over_sign = Object(center_x(screen_width)-game_over_sprite.get_width()/2, center_y(screen_height)-game_over_sprite.get_height()/2-100, 100, 100)
game_over_sign.force_image(game_over_sprite)
pricked_sprite = get_sprite(dino_sprite, 1689, 1, 88, 90)
cactus_brush_small5 = get_sprite(dino_sprite, 445, 1, 205, 75)
cactus_brush_small3 = get_sprite(dino_sprite, 445, 1, 102, 75)
cactus_brush_small2 = get_sprite(dino_sprite, 445, 1, 68, 75)
cactus_brush_small1 = get_sprite(dino_sprite, 445, 1, 34, 75)
cactus_brush_large2 = get_sprite(dino_sprite, 651, 1, 98, 100)
cactus_brush_large1 = get_sprite(dino_sprite, 651, 1, 49, 100)
cactus_brush_large4 = get_sprite(dino_sprite, 801, 1, 150, 100)
lovely_sprite = rotated(scaled(load_img(os.path.join('..', 'src', 'lovely.png')), 183, 160), 15)
lovely_sprite.set_alpha(10)
standing = get_sprite(dino_sprite, 1337, 6, 88, 90)
blinking = get_sprite(dino_sprite, 1425, 6, 88, 90)
walk1 = get_sprite(dino_sprite, 1513, 6, 88, 90)
walk2 = get_sprite(dino_sprite, 1601, 6, 88, 90)
walking_cluster = Cluster('walking', [standing, walk1, walk2])
ground_sprite = get_sprite(dino_sprite, 0, 103, 2401, 26)
idle_cluster = Cluster('idle', [standing, blinking])
ground1 = Object(0, 370, 2401, 1000)
ground2 = Object(2401, 370, 2401, 1000)
ground1.force_image(ground_sprite)
ground2.force_image(ground_sprite)
obstacles = [cactus_brush_small1, cactus_brush_small2, cactus_brush_small3, cactus_brush_large1, cactus_brush_large2, cactus_brush_large4]
dino = Object(x=100, y=200, width=90, height=90, clusters=[walking_cluster])
