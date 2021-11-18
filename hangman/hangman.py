import random
import pygame

pygame.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 800
PISMENO_VYSKA = 74
CERNA = (0, 0, 0)
BILA = (255, 255, 255)
podtrzitko_poz = [50, 300]
pismeno_poz = [60, 250]
podtrzitko_velikost = [50, 10]  # sířka, výška
posun = 0

vyber = ["pokus", "auto", "motorka", "autobus", "pes"]
nahodny = random.randint(0, len(vyber) - 1)
slovo = vyber[nahodny]
#  print(slovo)
pokusy = ""
spatne_pismeno = ""
poc_kol = 10

pygame.display.set_caption("Šibenice")
okno = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
okno.fill(CERNA)
for znak in slovo:
    pygame.draw.rect(okno, BILA, (podtrzitko_poz[0] + posun, podtrzitko_poz[1], podtrzitko_velikost[0], podtrzitko_velikost[1]))
    posun += 75

running = True
while running:
    pygame.time.delay(10)
    klavesa = pygame.key.get_pressed()
    udalosti = pygame.event.get()
    for event in udalosti:
        if event.type == pygame.QUIT:
            running = False

        elif klavesa[pygame.K_ESCAPE]:
            running = False

################################################### logika hry

    while poc_kol > 0:
        spatne = 0

        for znak in slovo:
            if znak in pokusy:
                print(znak)

            else:
                print("_")
                spatne += 1

        if spatne == 0:
            print("Vyhrál/a jsi")
            break

        pismeno = input("Tvůj tip: ")
        pokusy += pismeno

        if pismeno not in slovo:
            poc_kol -= 1
            print("Špatně!")
            print("Máš ještě", poc_kol, "pokusů")
            spatne_pismeno += pismeno
            print("Špatné typy: ", spatne_pismeno)

        if poc_kol == 0:
            print("Prohrál/a jsi")

##################################################
    okno.fill(CERNA)
    posun = 0
    font = pygame.font.Font(None, PISMENO_VYSKA)
    for znak in slovo:
        #pismeno = font.render(znak, True, BILA)
        pygame.draw.rect(okno, BILA, (podtrzitko_poz[0] + posun, podtrzitko_poz[1], podtrzitko_velikost[0], podtrzitko_velikost[1]))
        okno.blit(znak, (pismeno_poz[0] + posun, pismeno_poz[1]))
        posun += 75
    pygame.display.update()

pygame.quit()
