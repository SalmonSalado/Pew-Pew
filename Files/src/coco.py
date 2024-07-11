import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

run = True

pygame.mouse.set_visible(False)

ship = pygame.transform.scale(pygame.image.load('files/graphics/meteor.png').convert_alpha(), (32,32))
ship_rect = ship.get_rect()

ship_mask = pygame.mask.from_surface(ship)
mask_image = ship_mask.to_surface()


ship_rect.center = (50,50)

color = (0,255,0)

mouse_block = pygame.Surface((10,10))
mouse_block.fill(color)
mouse_rect = mouse_block.get_rect(center=pygame.mouse.get_pos())
mouse_mask = pygame.mask.from_surface(mouse_block)
while run:
    screen.fill((100,100,100))
    mouse_rect.center = pygame.mouse.get_pos()

    print(ship_mask.overlap(mouse_mask, (mouse_rect.x - ship_rect.x,mouse_rect.y - ship_rect.y)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                run = False
    mouse_block.fill(color)
    screen.blit(mask_image, ship_rect)
    screen.blit(mouse_block, mouse_rect)
    pygame.display.flip()
