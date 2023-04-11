import pgzrun

TITLE = "Brickbreaker"

WIDTH = 640
HEIGHT = 480

paddle = Actor("paddlered.png")
ball = Actor("ballgrey.png")
# Brick sprites are 64 by 32
brick_sprites = ["element_green_rectangle.png", "element_yellow_rectangle.png", "element_red_rectangle.png"]

def draw():
    screen.fill((100, 149, 237))
    paddle.x = 320
    paddle.y = 440
    paddle.draw()

    ball.x = 320
    ball.y = 340
    ball.draw()

    current_brick_pos_x = 64 / 2
    current_brick_pos_y = 32 / 2


    for brick_sprite in brick_sprites:
        place_brick(brick_sprite, current_brick_pos_x, current_brick_pos_y)
        current_brick_pos_y += 32

def place_brick(sprite, pos_x, pos_y):
    brick = Actor(sprite)
    brick.x = pos_x
    brick.y = pos_y
    brick.draw()

pgzrun.go()