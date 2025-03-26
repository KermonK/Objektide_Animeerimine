import pygame
import random

# Mängu akna suurus
WIDTH, HEIGHT = 640, 480 # Määrame ekraani laiuse ja kõrguse

# Initsialiseeri pygame
pygame.init() # Käivitame pygame'i
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Loome mänguakna
pygame.display.set_caption("Autode mäng")  # Seame akna nimeks "Autode mäng"

# Lae pildid
taust = pygame.image.load("bg_rally.jpg") # Laadime taustapildi
punane_auto = pygame.image.load("f1_red.png") # Laadime punase auto pildi
sinine_auto = pygame.image.load("f1_blue.png") # Laadime sinise auto pildi
sinine_auto = pygame.transform.rotate(sinine_auto, 180)  # Pöörame sinise auto tagurpidi

# Radajoonised (vahemik äärmistel radadel, mitte keskne rada)
VASAK_RADA_MIN, VASAK_RADA_MAX = 140, 200 # Vasakpoolse raja vahemik
PAREM_RADA_MIN, PAREM_RADA_MAX = 380, 450  # Parempoolse raja vahemik

# Autode parameetrid
punane_x = WIDTH // 2 - punane_auto.get_width() // 2  # Määrame punase auto x-positsiooni
punane_y = HEIGHT - punane_auto.get_height() - 20 # Määrame punase auto y-positsiooni
sinised_autod = [] # Loome nimekirja sinistest autodest
for _ in range(3): # Loome kolm sinist autot
    rada = random.choice([(VASAK_RADA_MIN, VASAK_RADA_MAX), (PAREM_RADA_MIN, PAREM_RADA_MAX)]) # Valime suvaliselt vasaku või parema raja
    x = random.randint(*rada) # Määrame sinise auto x-positsiooni suvaliselt valitud raja piires
    y = random.randint(-420, -130) # Määrame sinise auto algse y-positsiooni väljaspool ekraani
    sinised_autod.append([x, y]) # Lisame sinise auto listi

sinine_kiirus = 5 # Algne kiirus sinistele autodele
skor = 0 # Algne skoor

# Fondi seaded
font = pygame.font.Font(None, 36) # Loome fondi objekti

running = True # Mängu tsükkel jookseb seni, kuni running on True
while running:
    screen.blit(taust, (0, 0)) # Joonistame taustapildi ekraanile
    screen.blit(punane_auto, (punane_x, punane_y)) # Joonistame punase auto ekraanile

    for auto in sinised_autod: # Liigutame kõik sinised autod
        auto[1] += sinine_kiirus # Liigutame autot allapoole
        if auto[1] > HEIGHT: # Kui auto jõuab ekraani alla
            auto[1] = random.randint(-420, -130) # Paneme auto uuesti üles
            rada = random.choice([(VASAK_RADA_MIN, VASAK_RADA_MAX), (PAREM_RADA_MIN, PAREM_RADA_MAX)]) # Valime uue raja
            auto[0] = random.randint(*rada) # Määrame uue suvalise x-positsiooni valitud raja piires
            skor += 1 # Suurendame skoori ühe võrra
            sinine_kiirus += 0.5  # Suurendame kiirust iga läbimise järel
        screen.blit(sinine_auto, (auto[0], auto[1])) # Joonistame sinise auto ekraanile

    # Kuvame skoori
    skooritekst = font.render(f"Skoor: {skor}", True, (255, 255, 255)) # Loome skoori teksti
    screen.blit(skooritekst, (10, 10)) # Joonistame skoori ekraanile

    # Uuendame ekraani
    pygame.display.flip() # Värskendame ekraani

    for event in pygame.event.get(): # Läbime kõik sündmused
        if event.type == pygame.QUIT: # Kui kasutaja sulgeb akna
            running = False  # Lõpetame mängu tsükli

    pygame.time.delay(30) # Viivitus, et mäng ei jookseks liiga kiiresti


pygame.quit() # Sulgeme pygame'i
#updated 09:36