import pygame
lebar = 800
tinggi = 600
pygame.init()
layar = pygame.display.set_mode((lebar, tinggi))
selesai = False
biru = True

x = 30
y = 30

FPS = pygame.time.Clock()

while not selesai:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selesai = True

        if event.type == pygame.KEYDOWN  and event.key == pygame.K_SPACE:
            biru = not biru

    tekan = pygame.key.get_pressed()
    if tekan[pygame.K_UP]:
        y -= 3
    if tekan[pygame.K_DOWN]:
        y += 3
    if tekan[pygame.K_LEFT]:
        x -= 3
    if tekan[pygame.K_RIGHT]:
        x += 3

    layar.fill((239, 255, 255))

    if biru:
        warna = (0, 0, 255)
    else:
        warna = (251, 127, 80)

    pygame.draw.rect(layar, warna, pygame.Rect(x, y, 60, 60 ))
    pygame.display.flip()

    FPS.tick(60)