import pygame
import random

# Mängu akna suurus
WIDTH, HEIGHT = 640, 480

# Initsialiseeri pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autode mäng")

# Lae pildid
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")
sinine_auto = pygame.transform.rotate(sinine_auto, 180)  # Pöörame sinise auto tagurpidi

# Radajoonised (vahemik äärmistel radadel, mitte keskne rada)
VASAK_RADA_MIN, VASAK_RADA_MAX = 140, 200
PAREM_RADA_MIN, PAREM_RADA_MAX = 360, 440

# Autode parameetrid
punane_x = WIDTH // 2 - punane_auto.get_width() // 2
punane_y = HEIGHT - punane_auto.get_height() - 20
sinised_autod = []
for _ in range(3):
    rada = random.choice([(VASAK_RADA_MIN, VASAK_RADA_MAX), (PAREM_RADA_MIN, PAREM_RADA_MAX)])
    x = random.randint(*rada)
    y = random.randint(-420, -130)
    sinised_autod.append([x, y])

sinine_kiirus = 5
skor = 0

# Fondi seaded
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.blit(taust, (0, 0))
    screen.blit(punane_auto, (punane_x, punane_y))

    for auto in sinised_autod:
        auto[1] += sinine_kiirus
        if auto[1] > HEIGHT:
            auto[1] = random.randint(-420, -130)
            rada = random.choice([(VASAK_RADA_MIN, VASAK_RADA_MAX), (PAREM_RADA_MIN, PAREM_RADA_MAX)])
            auto[0] = random.randint(*rada)
            skor += 1
            sinine_kiirus += 0.5  # Suurendame kiirust iga läbimise järel
        screen.blit(sinine_auto, (auto[0], auto[1]))

    # Kuvame skoori
    skooritekst = font.render(f"Skoor: {skor}", True, (255, 255, 255))
    screen.blit(skooritekst, (10, 10))

    # Uuendame ekraani
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(30)

pygame.quit()
#updated 08:58