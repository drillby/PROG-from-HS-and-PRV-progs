import pygame

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Čtverečková hra')

black = (0, 0, 0)  # RGB+Alpha (Alpha - průhlednost)
white = (255, 255, 255)
blue = (0, 0, 255)

velikost_policka = 100


def pixely_to_mrizka(pixel_xy, rozmer_policka):
    return ( pixel_xy[0] // rozmer_policka, pixel_xy[1] // rozmer_policka )

def mrizka_to_rectangle(mrizka_xy, rozmer_policka):
    return (mrizka_xy[0]*rozmer_policka, mrizka_xy[1]*rozmer_policka, rozmer_policka, rozmer_policka)

def mrizka_to_stred(mrizka_xy, rozmer_policka):
    return (mrizka_xy[0]*rozmer_policka + rozmer_policka//2, mrizka_xy[1]*rozmer_policka + rozmer_policka//2)


hodiny = pygame.time.Clock()
fps = 10

screen.fill(white)

running = True
while running:
    # do fronty událostí pygame.event.get() se ukládají všechny události v průběhu jednoho frame
    for event in pygame.event.get():  # události -> start, quit, zmáčknutí klávesy, klik myší, pohyb myší, ...
        if event.type == pygame.QUIT:
            running = False
    
    # hodnoty stisknutých kláves v tomto aktuálnim okamžiku
    vsechny_klavesy = pygame.key.get_pressed()  # {K_a:True, K_b:False, K_c:True, .....}
    vsechna_tlacitka_mysi = pygame.mouse.get_pressed()  # (True, False, False)
    
    if vsechna_tlacitka_mysi[0]:
        pozice_mysi = pygame.mouse.get_pos()
        policko_souradnice = pixely_to_mrizka(pozice_mysi, velikost_policka)
        policko_obdelnik = mrizka_to_rectangle(policko_souradnice, velikost_policka)
        pygame.draw.rect(screen, blue, policko_obdelnik, 0)
        
        print("Tlacitko mysi 0 je zmacknute", pozice_mysi, pixely_to_mrizka(pozice_mysi, velikost_policka))
    

    hodiny.tick(fps)
    pygame.display.update()

pygame.quit()