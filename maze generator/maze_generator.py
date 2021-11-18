import pygame as pg
import random

OKNO_SIRKA = 800
OKNO_VYSKA = 800

SIRKA_BUNKY = 20
radky = OKNO_VYSKA/SIRKA_BUNKY
sloupce = OKNO_SIRKA/SIRKA_BUNKY

CERNA = (0, 0, 0)
BILA = (255, 255, 255)
NAVSTIVENO = (100, 175, 255)
ZELENA = (0, 255, 100)

fps = 60

zasobnik = []


class Bunka:
    def __init__(self, radek, sloupec):
        self.radek = radek
        self.sloupec = sloupec
        self.steny = [True, True, True, True]  # nahře, vpravo, dole, vlevo
        self.navstiveno = False

    def vykresli(self):
        x = self.radek*SIRKA_BUNKY
        y = self.sloupec*SIRKA_BUNKY

        if self.navstiveno:
            pg.draw.rect(okno, NAVSTIVENO, (x, y, SIRKA_BUNKY, SIRKA_BUNKY), 0)
            pg.draw.rect(okno, BILA, (x, y, SIRKA_BUNKY, SIRKA_BUNKY), -1)

        if self.steny[0]:
            pg.draw.line(okno, BILA, (x, y), (x + SIRKA_BUNKY, y))
        if self.steny[1]:
            pg.draw.line(okno, BILA, (x + SIRKA_BUNKY, y),
                         (x + SIRKA_BUNKY, y + SIRKA_BUNKY))
        if self.steny[2]:
            pg.draw.line(okno, BILA, (x + SIRKA_BUNKY, y +
                                      SIRKA_BUNKY), (x, y + SIRKA_BUNKY))
        if self.steny[3]:
            pg.draw.line(okno, BILA, (x, y + SIRKA_BUNKY), (x, y))

    def zkontrolujSousedy(self):
        sousedi = []

        index_nahore = zjistiIndex(self.radek, self.sloupec - 1)
        index_vpravo = zjistiIndex(self.radek + 1, self.sloupec)
        index_dole = zjistiIndex(self.radek, self.sloupec + 1)
        index_vlevo = zjistiIndex(self.radek - 1, self.sloupec)

        nahore = bunky[int(index_nahore)] if index_nahore is not None else None
        vpravo = bunky[int(index_vpravo)] if index_vpravo is not None else None
        dole = bunky[int(index_dole)] if index_dole is not None else None
        vlevo = bunky[int(index_vlevo)] if index_vlevo is not None else None

        if nahore is not None and not nahore.navstiveno:
            sousedi.append(nahore)
        if vpravo is not None and not vpravo.navstiveno:
            sousedi.append(vpravo)
        if dole is not None and not dole.navstiveno:
            sousedi.append(dole)
        if vlevo is not None and not vlevo.navstiveno:
            sousedi.append(vlevo)

        if len(sousedi) > 0:
            r = random.choice(sousedi)
            return r
        else:
            return None

    def zvyrazni(self):
        x = self.radek*SIRKA_BUNKY
        y = self.sloupec*SIRKA_BUNKY

        pg.draw.rect(okno, ZELENA, (x, y, SIRKA_BUNKY, SIRKA_BUNKY), 0)


def zjistiIndex(i, j):
    if i < 0 or j < 0 or i > sloupce - 1 or j > radky - 1:
        return None

    return i + j * sloupce


def odstranSteny(a, b):
    x = a.radek - b.radek
    if x == 1:
        a.steny[3] = False
        b.steny[1] = False
    elif x == -1:
        a.steny[1] = False
        b.steny[3] = False

    y = a.sloupec - b.sloupec
    if y == 1:
        a.steny[0] = False
        b.steny[2] = False
    elif y == -1:
        a.steny[2] = False
        b.steny[0] = False


pg.init()

hodiny = pg.time.Clock()

pg.display.set_caption("Maze generation algoritmus")
okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
okno.fill(CERNA)

bunky = []
for j in range(int(radky)):
    for i in range(int(sloupce)):
        bunka = Bunka(i, j)
        bunky.append(bunka)
soucasna = bunky[0]

running = True
while running:
    klavesa = pg.key.get_pressed()
    udalosti = pg.event.get()
    for event in udalosti:
        if event.type == pg.QUIT:
            running = False

        elif klavesa[pg.K_ESCAPE]:
            running = False

    for objekt in bunky:
        objekt.vykresli()

    soucasna.navstiveno = True
    soucasna.zvyrazni()
    dalsi = soucasna.zkontrolujSousedy()
    if dalsi:
        dalsi.navstiveno = True
        zasobnik.append(soucasna)
        odstranSteny(soucasna, dalsi)
        soucasna = dalsi
    elif len(zasobnik) > 0:
        soucasna = zasobnik.pop(len(zasobnik) - 1)

    hodiny.tick(fps)
    pg.display.update()

pg.quit()
