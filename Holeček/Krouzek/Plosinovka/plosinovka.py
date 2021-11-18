import pygame
from pygame.locals import *

pygame.init()

OKNO_SIRKA = 800
OKNO_VYSKA = 600

CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)

TIHOVE_ZRYCHLENI_VE_HRE = 10

pozice_font = pygame.font.Font(None, 25)


class Hrac:
    def __init__(self, zadane_jmeno, zadany_prumer, zadana_pozice_x, zadana_pozice_y, barva):
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 # desítková soustava
        # 0 1 2 3 4 5 6 7 8 9 A B C D E F # šestnáctková soustava
        #    IIII - jednotková soustava (unární)

        self.jmeno = zadane_jmeno
        self.prumer = zadany_prumer
        self.pozice_x = zadana_pozice_x
        self.pozice_y = zadana_pozice_y
        self.barva = barva
        self.rychlost_x = 0
        self.rychlost_y = 0

    # Zapouzdření
    @property  # Getter (i v jiných jazycích)
    def pozice_y(self):
        return self.__pozice_y

    @pozice_y.setter  # Setter (i v jiných jazycích)
    def pozice_y(self, nova_hodnota):
        if nova_hodnota < 0 + self.prumer // 2:
            self.__pozice_y = 0 + self.prumer // 2
        elif nova_hodnota > OKNO_VYSKA - self.prumer // 2:
            self.__pozice_y = OKNO_VYSKA - self.prumer // 2
        else:
            self.__pozice_y = nova_hodnota

    @property  # Getter (i v jiných jazycích)
    def pozice_x(self):
        return self.__pozice_x

    @pozice_x.setter  # Setter (i v jiných jazycích)
    def pozice_x(self, nova_hodnota):
        if nova_hodnota < 0 + self.prumer // 2:
            self.__pozice_x = 0 + self.prumer // 2
        elif nova_hodnota > OKNO_SIRKA - self.prumer // 2:
            self.__pozice_x = OKNO_SIRKA - self.prumer // 2
        else:
            self.__pozice_x = nova_hodnota

    def pohni_se(self, za_jakou_dobu):
        # s = s0 + v*t
        print(self.rychlost_x)
        self.pozice_x = self.pozice_x + (self.rychlost_x * za_jakou_dobu / 1000)  # cas je vzdy jeden frame
        self.pozice_y = self.pozice_y - (self.rychlost_y * za_jakou_dobu / 1000)
        self.rychlost_y = self.rychlost_y - TIHOVE_ZRYCHLENI_VE_HRE

    def skok(self):
        print("Skaču")
        self.rychlost_x = 5
        self.rychlost_y = 50

    def zobraz(self, platno_kam):
        kolecko_obdelnik = pygame.draw.circle(platno_kam, self.barva, [int(self.pozice_x), int(self.pozice_y)], self.prumer // 2, 0)

        # Doděláme - zobrazuje text
        # text = pygame.font.render('x: {} y: {}'.format(CarPos[0], CarPos[1]), True, black, white)
        # textRect = text.get_rect()
        # textRect.center = (display_width // 2, 20)
        # platno_kam.blit(text, textRect)
        return kolecko_obdelnik

    def pohyb_vpravo(self):
        self.pozice_x += 10  # self.pozice_x = self.pozice_x + 10
        self.rychlost_x = 0

    def pohyb_vlevo(self):
        self.pozice_x -= 10
        self.rychlost_x = 0

    def pohyb_nahoru(self):
        self.pozice_y -= 10
        self.rychlost_y = 0

    def pohyb_dolu(self):
        self.pozice_y += 10
        self.rychlost_y = 0


platno_hlavni = pygame.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))
pygame.display.set_caption('Krouzek - plosinovka')

zetony = pygame.image.load("pictures/zetony.jpg").convert()
zetony = pygame.transform.scale(zetony, (OKNO_SIRKA, OKNO_VYSKA))

# >>> Funkce convert() upravi data tak, aby je Pygame mohl rychle vykreslovat -> tedy ji chceme používat :-)
karta = pygame.image.load("pictures/karta.jpg").convert_alpha()
karta_obdelnik = karta.get_rect()
karta = pygame.transform.scale(karta, (karta_obdelnik[2] // 5, karta_obdelnik[3] // 5))

hrac1 = Hrac("Franta", 100, 200, 400, (0, 0, 0))
hrac2 = Hrac("Tonda", 200, 400, 600, (255, 0, 0))

#  Nakresleni zacatku hry
platno_hlavni.blit(zetony, (0, 0))

hrac1_obdelnik = hrac1.zobraz(platno_hlavni)
# hrac2_obdelnik = hrac2.zobraz(platno_hlavni)

auto_obdelnik = platno_hlavni.blit(karta, dest=(50, 400), area=None)

text = pozice_font.render('x: {} y: {}'.format(hrac1.pozice_x, hrac1.pozice_y), True, CERNA, None)
textRect = text.get_rect()
textRect.center = (OKNO_SIRKA // 2, textRect[2])  # textRect[2] výška obdélníku
textRect_toRemove = platno_hlavni.blit(text, dest=textRect)

naposledy_jsem_kreslil_v = pygame.time.get_ticks()

hodiny = pygame.time.Clock()
fps = 20
# key_interval = 500//fps
# pygame.key.set_repeat(key_interval, key_interval)
running = True
while running:
    # Ukladá si fo fronty všechny události a zpracuje je ve chvíli, kdy doběhne na tento řádek (tedy i ty, které se staly kdykoliv v průběhu programu)
    udalosti = pygame.event.get()
    for event in udalosti:
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        # if event.key == K_d:
        #     kolecko_stred[0] = kolecko_stred[0] + posun_kolecka
        # elif event.key == K_a:
        #     kolecko_stred[0] = kolecko_stred[0] - posun_kolecka
        # elif event.key == K_s:
        #     kolecko_stred[1] = kolecko_stred[1] + posun_kolecka
        # elif event.key == K_w:
        #     kolecko_stred[1] = kolecko_stred[1] - posun_kolecka

    # Ziskam aktualne stisknute klavesy (stisknute ve chvili, kdy je program na tomto řádku)
    stisknute_klavesy = pygame.key.get_pressed()  # [K_Q:False K_W:False K_E:True K_R:False K_esc:false]
    if stisknute_klavesy[K_d]:  # True == True -> True    False == True -> False --> Záleží jen na prvním
        hrac1.pohyb_vpravo()
        # hrac2.pohyb_vpravo()
    if stisknute_klavesy[K_a]:
        hrac1.pohyb_vlevo()
        # hrac2.pohyb_vlevo()
    if stisknute_klavesy[K_s]:
        hrac1.pohyb_dolu()
        # hrac2.pohyb_dolu()
    if stisknute_klavesy[K_w]:
        hrac1.pohyb_nahoru()
        # hrac2.pohyb_nahoru()
    if stisknute_klavesy[K_q]:
        hrac1.skok()

    # hrac1.pozice_y = -25  # -> Spustí funkci pozice_y(self, nova_hodnota): která je @pozice_y.setter
    # 1) Existuje proměná hrac1.pozice_y ? Ne
    #       Co teda existuje ? I) Existuje funkce pozice_y() jako @pozice_y.setter
    #                          II) Existuje to, co jsem vyrobil ve funkci pozice_y() -> takže u nás proměnná __pozice_y
    #       Co k čertu znamenají ty __ ? Proměnná je schovaná -> nemůžu jí číst ani do ní zapisovat mimo třídu ve které existuje

    # print(hrac1.pozice_y) # -> Spustí funkci pozice_y(self): která je @property

    # print(pygame.time.get_ticks())
    aktualni_cas = pygame.time.get_ticks()
    kolik_casu_ubehlo = aktualni_cas - naposledy_jsem_kreslil_v
    naposledy_jsem_kreslil_v = aktualni_cas

    hrac1.pohni_se(kolik_casu_ubehlo)

    text = pozice_font.render('x: {} y: {}'.format(hrac1.pozice_x, hrac1.pozice_y), True, CERNA, None)
    textRect = text.get_rect()
    textRect.center = (OKNO_SIRKA // 2, textRect[2])  # textRect[2] výška obdélníku
    platno_hlavni.blit(zetony, dest=textRect_toRemove, area=textRect_toRemove)
    textRect_toRemove = platno_hlavni.blit(text, dest=textRect)

    ax1 = auto_obdelnik[0]
    ax2 = auto_obdelnik[0] + auto_obdelnik[2]

    # print(hrac1_obdelnik)
    hx1 = hrac1_obdelnik[0]
    hx2 = hrac1_obdelnik[0] + hrac1_obdelnik[2]

    if (hx1 >= ax1 and hx1 <= ax2) or (hx2 >= ax1 and hx2 <= ax2) or (hx1 < ax1 and hx2 > ax2):
        hrac1.barva = CERVENA
    else:
        hrac1.barva = CERNA

    # # zmena smeru pohybu
    # if (kolecko_stred[0] + kolecko_polomer >= okno_sirka) or (kolecko_stred[0] - kolecko_polomer <= 0):
    #     posun_kolecka = -posun_kolecka

    # pracuje s autem
    platno_hlavni.blit(zetony, dest=auto_obdelnik, area=auto_obdelnik)  # "ctrl+C ctrl+V"
    auto_obdelnik = platno_hlavni.blit(karta, dest=(50, 400), area=None)  # Vloží celý (area=None) obrázek auto do platno_hlavni na pozici (50, 200)

    # pracuje s koleckem
    platno_hlavni.blit(zetony, dest=hrac1_obdelnik, area=hrac1_obdelnik)  # "ctrl+C ctrl+V"
    hrac1_obdelnik = hrac1.zobraz(platno_hlavni)

    # platno_hlavni.blit(mraky, dest=hrac2_obdelnik, area=hrac2_obdelnik)  # "ctrl+C ctrl+V"
    # hrac2_obdelnik = hrac2.zobraz(platno_hlavni)

    hodiny.tick(fps)
    pygame.display.flip()  # překreslí celý obraz
    # pygame.display.display(oblast_se_zmenou)

pygame.quit()
