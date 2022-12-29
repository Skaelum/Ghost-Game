import pygame
import spritesheet

pygame.init()
width = 900
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ghost Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

Ghost = pygame.image.load("ghost.png")
Ghost = pygame.transform.scale(Ghost, (100, 100))
Ghost_x = 20
Ghost_y = 580

Black = (0, 0, 0)


sprite_sheet_image = pygame.image.load("portal_green.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)


def display_ghost(x, y):
    window.blit(Ghost, (x, y))


def portal():
    window.blit(animation_list[frame], (360, 270))


animation_list = []
animation_steps = 90
last_update = pygame.time.get_ticks()
animation_cooldown = 25
frame = 0

for a in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(a, 70, 60, 2, Black))

portal_display = window.blit(animation_list[frame], (0, 0))

GameOn = True
while GameOn:

    window.fill((93, 109, 126))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_i] and keys[pygame.K_c] and keys[pygame.K_y]:
        portal()

    if Ghost_x > width:
        Ghost_x = 900
    if Ghost_y > width:
        Ghost_y = 700
    if Ghost_x < 0:
        Ghost_x = 0
    if Ghost_y < 0:
        Ghost_y = 0

    if keys[pygame.K_a]:
        if keys[pygame.K_w]:
            Ghost_y -= .5
            Ghost_x -= .5
        elif keys[pygame.K_s]:
            Ghost_y += .5
            Ghost_x -= .5
        else:
            Ghost_x -= 0.3
    if keys[pygame.K_d]:
        if keys[pygame.K_w]:
            Ghost_y -= .5
            Ghost_x += .5
        elif keys[pygame.K_s]:
            Ghost_y += .5
            Ghost_x += .5
        else:
            Ghost_x += 0.3
    if keys[pygame.K_w]:
        Ghost_y -= 0.3
    if keys[pygame.K_s]:
        Ghost_y += 0.3

    display_ghost(Ghost_x, Ghost_y)
    pygame.display.update()

pygame.quit()
