import pygame
import numpy as np

pygame.init()

SPUSTENO = False

SIRKA_OKNA = 1200
VYSKA_OKNA = 800

okno = pygame.display.set_mode((SIRKA_OKNA, VYSKA_OKNA))
pygame.display.set_caption("Game of life")

CERNA = (0, 0, 0)
BILA = (255, 255, 255)
CERVENA = (255, 0, 0)

velikost_policka = 20

stare_bunky = np.random.randint(
    1, size=(SIRKA_OKNA // velikost_policka, VYSKA_OKNA // velikost_policka)
)  # 2D pole, má náhodné hodnoty buňek na obou osách

nove_bunky = np.empty(
    (SIRKA_OKNA // velikost_policka, VYSKA_OKNA // velikost_policka)
)  # prázdné 2D pole

try:
    with open("s.txt", "r") as input_file:
        for radek in input_file:
            souradnice = list(map(int, radek.split(" ")))
            stare_bunky[souradnice[0], souradnice[1]] = 1

except FileNotFoundError:
    print("Soubor start.txt nenalezen. Pokud chceš číst ze souboru vytvoř start.txt.")

font = pygame.font.Font(None, 12)


def spocitejSousedy(tabulka_bunek, x, y):
    pocet = 0
    for x2 in range(-1, 2):
        for y2 in range(-1, 2):
            pocet += tabulka_bunek[x + x2][y + y2]

    pocet -= tabulka_bunek[x][y]
    # print(pocet)
    return int(pocet)


def ziskejPozici(pozice, policko):
    return pozice[0] // policko, pozice[1] // policko


def vykresliStare():
    okno.fill(BILA)
    for i in range((SIRKA_OKNA // velikost_policka)):
        for j in range((VYSKA_OKNA // velikost_policka)):
            if stare_bunky[i][j] == 1:
                pygame.draw.rect(
                    okno,
                    CERNA,
                    (
                        i * velikost_policka,
                        j * velikost_policka,
                        velikost_policka,
                        velikost_policka,
                    ),
                    0,
                )
    pygame.display.update()


hodiny = pygame.time.Clock()
fps = 10

vykresliStare()

running = True
while running:
    vsechny_klavesy = pygame.key.get_pressed()
    pozice_mysi = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        bunka_x, bunka_y = ziskejPozici(pozice_mysi, velikost_policka)
        # print(bunka_x, bunka_y)
        stare_bunky[bunka_x][bunka_y] = 1
        nove_bunky[bunka_x][bunka_y] = 1

        vykresliStare()

    okno.fill(BILA)
    if vsechny_klavesy[pygame.K_SPACE] or SPUSTENO:  # spustí simulaci
        SPUSTENO = True
        for i in range(SIRKA_OKNA // velikost_policka):
            for j in range(VYSKA_OKNA // velikost_policka):
                stav = stare_bunky[i][j]  # nahraje stav buňky na i, j do stavu
                # když okraj, nic se nemění
                if (
                    i == 0
                    or i == (SIRKA_OKNA // velikost_policka) - 1
                    or j == 0
                    or j == (VYSKA_OKNA // velikost_policka) - 1
                ):
                    nove_bunky[i][j] = stav
                else:
                    sousedi = spocitejSousedy(stare_bunky, i, j)

                    if stav == 1 and (sousedi < 2 or sousedi > 3):
                        nove_bunky[i][j] = 0
                    elif stav == 0 and sousedi == 3:
                        nove_bunky[i][j] = 1
                    else:
                        nove_bunky[i][j] = stav

                    text = font.render(str(sousedi), True, CERVENA)
                    okno.blit(
                        text,
                        (
                            i * velikost_policka + velikost_policka // 2,
                            j * velikost_policka + velikost_policka // 2,
                        ),
                    )

        for i in range((SIRKA_OKNA // velikost_policka)):
            for j in range((VYSKA_OKNA // velikost_policka)):
                if nove_bunky[i][j] == 1:
                    pygame.draw.rect(
                        okno,
                        CERNA,
                        (
                            i * velikost_policka,
                            j * velikost_policka,
                            velikost_policka,
                            velikost_policka,
                        ),
                        0,
                    )

        stare_bunky = nove_bunky.copy()
        hodiny.tick(fps)
        pygame.display.update()

pygame.quit()


with open("konec.txt", "w") as output_file:
    for i in range((SIRKA_OKNA // velikost_policka)):
        for j in range((VYSKA_OKNA // velikost_policka)):
            if nove_bunky[i][j] == 1:
                output_file.write("{} {}\n".format(i, j))
