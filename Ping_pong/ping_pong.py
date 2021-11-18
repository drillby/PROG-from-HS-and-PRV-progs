import pygame

pygame.init()

OKNO_SIRKA = 1000
OKNO_VYSKA = 600

CERNA = (0, 0, 0)
BILA = (255, 255, 255)
RYCHLOST_HRAC = 10
RYCHLOST_MICEK = [5, 5]
VYSKA_HRAC = 150
SIRKA_HRAC = 20
STRANA_MICEK = 20
MAX_SCORE = 10
ODRAZ_ZVUK = pygame.mixer.Sound("Ping_pong\odraz.wav")

frame_counter = 0

hrac1_poz = [25, 225]
hrac2_poz = [950, 225]
micek_poz = [500, 300]

hrac1_score = 0
hrac2_score = 0

font = pygame.font.Font(None, 74)
pygame.display.set_caption("Ping-Pong")
okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

okno.fill(CERNA)
# kam, barva, souřadnice, velikost
hrac1 = pygame.draw.rect(
    okno, BILA, (hrac1_poz[0], hrac1_poz[1], SIRKA_HRAC, VYSKA_HRAC))
hrac2 = pygame.draw.rect(
    okno, BILA, (hrac2_poz[0], hrac2_poz[1], SIRKA_HRAC, VYSKA_HRAC))
micek = pygame.draw.rect(
    okno, BILA, (micek_poz[0], micek_poz[1], STRANA_MICEK, STRANA_MICEK))

hodiny = pygame.time.Clock()
fps = 60

# // zjistit pozici míčku
# // na 10 snímku dopředu spočítat pozici míčku:
# // odrazy od horní a dolní stěny
# // odraz od hráče ovládanýho člověkem
# // zjistit pozici kam by se bot měl přesunout
#  TODO: přijít na to jak implementovat výslednou lokaci do hry bez porušení dané rychlosti hráče
# ? mohlo by fungovat přes if zjistim jestli jsem nad, nebo pod míčkem a pak přes while čekat než dojede na správnou pozici
# TODO: divnej odraz na y, u hrac2 divnej odraz


def bot(micek_pozice, sirka_hrac, vyska_hrac, strana_micek, rychlost_micek, rychlost_hrac, okno_sirka, okno_vyska, hrac1_pozice):
    for _ in range(10):
        micek_pozice[0] += rychlost_micek[0]
        micek_pozice[1] += rychlost_micek[1]
        hrac2_pozice = [950, 0]

        if micek_pozice[0] - sirka_hrac <= hrac1_pozice[0] and micek_pozice[1] in range(hrac1_pozice[1], hrac1_pozice[1] + vyska_hrac):
            if rychlost_micek[0] < 0:
                rychlost_micek[0] -= rychlost_micek[0]

            elif rychlost_micek[0] > 0:
                rychlost_micek[0] += 1

            if rychlost_micek[1] < 0:
                rychlost_micek[1] -= rychlost_micek[0]

            elif rychlost_micek[1] > 0:
                rychlost_micek[1] += 1

            rychlost_micek[0] -= rychlost_micek[0]

        if micek_pozice[0] + sirka_hrac >= hrac2_pozice[0] and micek_pozice[1] in range(hrac2_pozice[1], hrac2_pozice[1] + okno_vyska):
            if rychlost_micek[0] < 0:
                rychlost_micek[0] -= 1

            elif rychlost_micek[0] > 0:
                rychlost_micek[0] += 1

            if rychlost_micek[1] < 0:
                rychlost_micek[1] -= rychlost_micek[0]

            elif rychlost_micek[1] > 0:
                rychlost_micek[1] += 1

        if micek_pozice[1] + strana_micek >= okno_vyska:
            rychlost_micek[1] = - rychlost_micek[1]

        if micek_pozice[1] - strana_micek <= 0:
            rychlost_micek[1] = - rychlost_micek[1]

    micek_pozice_10_framu_vic = micek_pozice

    return micek_pozice_10_framu_vic


running = True
while running:
    klavesa = pygame.key.get_pressed()
    udalosti = pygame.event.get()
    for event in udalosti:
        if event.type == pygame.QUIT:
            running = False

        elif klavesa[pygame.K_ESCAPE]:
            running = False

    frame_counter += 1

    print("micek ted", micek_poz)
    if frame_counter % 10 == 0:
        print("micek 10 framu dopredu", bot(micek_poz.copy(), SIRKA_HRAC, VYSKA_HRAC,
                                            STRANA_MICEK, RYCHLOST_MICEK, RYCHLOST_HRAC, OKNO_SIRKA, OKNO_VYSKA, hrac1_poz))
    #  něco to počítá, ale nejsem si jistej jestli správně
    #  když si napočítám 10 "micek ted", tak to nesedi s 1. "micek 10 framu dopredu"
    #  plus celá hra je strašně zrychlená, nevím jak fixnout

    micek_poz[1] += RYCHLOST_MICEK[1]
    micek_poz[0] += RYCHLOST_MICEK[0]

    if micek_poz[0] - SIRKA_HRAC <= hrac1_poz[0] and micek_poz[1] in range(hrac1_poz[1], hrac1_poz[1] + VYSKA_HRAC):
        if RYCHLOST_MICEK[0] < 0:
            RYCHLOST_MICEK[0] -= 1

        elif RYCHLOST_MICEK[0] > 0:
            RYCHLOST_MICEK[0] += 1

        if RYCHLOST_MICEK[1] < 0:
            RYCHLOST_MICEK[1] -= 1

        elif RYCHLOST_MICEK[1] > 0:
            RYCHLOST_MICEK[1] += 1

        RYCHLOST_MICEK[0] = - RYCHLOST_MICEK[0]
        ODRAZ_ZVUK.play()

    if micek_poz[0] + SIRKA_HRAC >= hrac2_poz[0] and micek_poz[1] in range(hrac2_poz[1], hrac2_poz[1] + VYSKA_HRAC):
        if RYCHLOST_MICEK[0] < 0:
            RYCHLOST_MICEK[0] -= 1

        elif RYCHLOST_MICEK[0] > 0:
            RYCHLOST_MICEK[0] += 1

        if RYCHLOST_MICEK[1] < 0:
            RYCHLOST_MICEK[1] -= 1

        elif RYCHLOST_MICEK[1] > 0:
            RYCHLOST_MICEK[1] += 1

        RYCHLOST_MICEK[0] = - RYCHLOST_MICEK[0]
        ODRAZ_ZVUK.play()

    if micek_poz[1] + STRANA_MICEK >= OKNO_VYSKA:
        RYCHLOST_MICEK[1] = - RYCHLOST_MICEK[1]
        ODRAZ_ZVUK.play()

    if micek_poz[1] - STRANA_MICEK <= 0:
        RYCHLOST_MICEK[1] = - RYCHLOST_MICEK[1]
        ODRAZ_ZVUK.play()

    if klavesa[pygame.K_w] and hrac1_poz[1] >= 0:
        hrac1_poz[1] -= RYCHLOST_HRAC

    if klavesa[pygame.K_s] and hrac1_poz[1] <= OKNO_VYSKA - VYSKA_HRAC:
        hrac1_poz[1] += RYCHLOST_HRAC

    if klavesa[pygame.K_UP] and hrac2_poz[1] >= 0:
        hrac2_poz[1] -= RYCHLOST_HRAC

    if klavesa[pygame.K_DOWN] and hrac2_poz[1] <= OKNO_VYSKA - VYSKA_HRAC:
        hrac2_poz[1] += RYCHLOST_HRAC

    if micek_poz[0] <= 0:
        hrac1_score += 1
        micek_poz = [500, 300]
        RYCHLOST_MICEK = [5, 5]

    if micek_poz[0] >= OKNO_SIRKA - STRANA_MICEK:
        hrac2_score += 1
        micek_poz = [500, 300]
        RYCHLOST_MICEK = [5, 5]

    if hrac1_score == MAX_SCORE or hrac2_score == MAX_SCORE:
        micek_poz = [500, 300]
        RYCHLOST_MICEK = [0, 0]

    # hrac2_poz[1] = micek_poz[1] - 50

    text1 = font.render(str(hrac1_score), True, BILA)
    text2 = font.render(str(hrac2_score), True, BILA)
    okno.fill(CERNA)
    # kam, barva, souřadnice, velikost
    pygame.draw.rect(
        okno, BILA, (hrac1_poz[0], hrac1_poz[1], SIRKA_HRAC, VYSKA_HRAC))
    pygame.draw.rect(
        okno, BILA, (hrac2_poz[0], hrac2_poz[1], SIRKA_HRAC, VYSKA_HRAC))
    pygame.draw.rect(
        okno, BILA, (micek_poz[0], micek_poz[1], STRANA_MICEK, STRANA_MICEK))
    okno.blit(text2, (200, 50))
    okno.blit(text1, (800, 50))
    if hrac1_score == MAX_SCORE or hrac2_score == MAX_SCORE:
        text_konec = font.render("Konec hry", True, BILA)
        okno.blit(text_konec, (400, 50))

    hodiny.tick(fps)
    pygame.display.update()

pygame.quit()
