import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

run = True

ship = pygame.transform.scale(pygame.image.load('files/graphics/shooter.png').convert_alpha(), (32,32))
ship_rect = ship.get_rect()

ship_rect.center = (50,50)

rotated_ship = ship
rotated_ship_rect = ship_rect

start_time = pygame.time.get_ticks()
delay = 500
angle = 0

def rotate_img(image, topleft, angle):
    center = image.get_rect(topleft = topleft).center
    rotated_img = pygame.transform.rotate(image, angle)
    new_rect = rotated_img.get_rect(center=center)

    return rotated_img , new_rect 

while run:
    current_time = pygame.time.get_ticks()
    screen.fill('black')
   
    if angle > 360: angle = 0
    

    if current_time - start_time > delay:
        start_time = current_time
        angle += 90
        rotated_ship , rotated_ship_rect = rotate_img(ship, ship_rect.topleft, angle) 

    print(angle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False

    screen.blit(rotated_ship, rotated_ship_rect) 
    pygame.display.flip()
