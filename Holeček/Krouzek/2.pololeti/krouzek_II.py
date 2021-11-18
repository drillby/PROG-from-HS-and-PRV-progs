import pygame
from pygame.locals import *
pygame.init()

# Na motivy Rostislava


def najdi_kolecko(pozice, vsechna_kolecka):
    chycena_kolecka = []
    for kolecko in vsechna_kolecka:
        if kolecko.getCtverec().collidepoint(pozice):
            chycena_kolecka.append(kolecko)
    return chycena_kolecka


# OOP - Objektově orientované programování
class Kolecko:
    def __init__(self, zadany_stred, zadana_velikost, zadana_rychlost):
        """
        :param pozice: [x,y]
        :param posun: [posun_x, posun_y]
        """
        self.stred = zadany_stred

        # self.polomer = 10 if zadana_velikost < 10 else zadana_velikost
        self.polomer = max(10, zadana_velikost)
        self.rychlost = zadana_rychlost

    def posun_se(self):
        self.stred[0] += self.rychlost[0]
        self.stred[1] += self.rychlost[1]

    def getCtverec(self):
        return pygame.Rect(self.stred[0]-self.polomer, self.stred[1]-self.polomer, 2*self.polomer, 2*self.polomer)


OKNO_SIRKA = 500
OKNO_VYSKA = 300
BLUE = (0, 0, 255)  # RGB
WHITE = (255, 255, 255)

platno_hlavni = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
pygame.display.set_caption('Klub II')

vsechna_kolecka = []  # [ Kolecko 1, Kolecko 2, Kolecko 3, ... ]

hodiny = pygame.time.Clock()
fps = 3

aktualni_cas = pygame.time.get_ticks()
merim_delku_stisknuti = False

running = True  # True/False (datový typ boolean)
while running:  # while-cyklus (spustí odsazené příkazy vždy, kduž je v podmínce True)
    # Ukladá si fo fronty všechny události a zpracuje je ve chvíli, kdy doběhne na tento řádek (tedy i ty, které se staly kdykoliv v průběhu programu)
    udalosti = pygame.event.get()  # seznam událostí
    for event in udalosti:  # for-cyklus prochází všechny prvky v seznamu
        if event.type == pygame.QUIT:  # if spustí příkazy pouze pokud je podmínka splněná
            running = False

        # reakce na stisk (klávesa změní stav z neznáčknuto na zmáčknuto)
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                pass

        # if event.type == pygame.MOUSEBUTTONDOWN:  # reakce na stisk (klávesa změní stav z neznáčknuto na zmáčknuto)
        #     if event.button == 1:  # 1 leve tlacitko mysi, 2 prostřední, 3 pravé.
        #         if not najdi_kolecko(event.pos, vsechna_kolecka):  # prázdný list se bere jako False
        #             vsechna_kolecka.append( Kolecko(list(event.pos), 20, [5, 10]) )

    # měřit čas od zmáčknutí po puštění

    platno_hlavni.fill(WHITE)

    # {K_Q:False, K_W:False, K_E:True, K_R:False, K_esc:False, ...}
    stisknute_klavesy = pygame.key.get_pressed()
    if stisknute_klavesy[K_a]:
        pass

    # tlacitka_mysi = pygame.mouse.get_pressed()  # [False, False, True]
    # if tlacitka_mysi[0]:
    #     # pozice_mysi = pygame.mouse.get_pos()  # [x,y]
    #     # pygame.draw.circle(platno_hlavni, BLUE, pozice_mysi, 20, 4)
    #     pass

    tlacitka_mysi = pygame.mouse.get_pressed()  # [False, False, True]
    if tlacitka_mysi[0]:
        pozice_mysi = list(pygame.mouse.get_pos())  # [x,y]
        chycena_kolecka = najdi_kolecko(pozice_mysi, vsechna_kolecka)
        if not chycena_kolecka and not merim_delku_stisknuti:
            merim_delku_stisknuti = True
            zacatek_stisknuti = pygame.time.get_ticks()

        for chycene_kolecko in chycena_kolecka:
            chycene_kolecko.stred = pozice_mysi
    else:  # nezmacknuta mys
        if merim_delku_stisknuti:
            konec_stisknuti = pygame.time.get_ticks()
            merim_delku_stisknuti = False

            # Vyrobit kolecko + nastavit velikost kolecka podle doby stisnutí
            pozice_mysi = list(pygame.mouse.get_pos())  # [x,y]
            # cas se meri v milisekundách
            velikost_kolecka = (konec_stisknuti-zacatek_stisknuti)//50
            vsechna_kolecka.append(
                Kolecko(pozice_mysi, velikost_kolecka, [5, 10]))

    for kolecko in vsechna_kolecka:
        if kolecko.stred[0] >= OKNO_SIRKA or kolecko.stred[0] <= 0:
            # zmena smeru x
            kolecko.rychlost[0] *= -1

        if kolecko.stred[1] >= OKNO_VYSKA or kolecko.stred[1] <= 0:
            # zmena smeru y
            kolecko.rychlost[1] *= -1

        pygame.draw.circle(platno_hlavni, BLUE,
                           kolecko.stred, kolecko.polomer, 4)
        kolecko.posun_se()

    pygame.display.update()
    # předchozí zavolání v 26s další zavolání v 26,00002s -> počká do 26,1s a teprve poté "pustí" program dál
    hodiny.tick(fps)

pygame.quit()
