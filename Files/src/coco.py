import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

run = True

ship = pygame.transform.scale(pygame.image.load('files/graphics/shooter.png').convert_alpha(), (32,32))
ship_rect = ship.get_rect()

ship_rect.center = (50,50)

color = (0,255,0)

mouse_block = pygame.Surface((1,1))
mouse_block.fill(color)
mouse_rect = mouse_block.get_rect(center=pygame.mouse.get_pos())

while run:
    screen.fill((100,100,100))
    mouse_rect.center = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False

    screen.blit(pygame.mask.from_surface(ship).to_surface() , ship_rect)
    screen.blit(mouse_block, mouse_rect)
    pygame.display.flip()
