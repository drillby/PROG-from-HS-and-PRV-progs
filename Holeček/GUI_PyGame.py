import pygame

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Super hra')

black = (0, 0, 0)  # RGB+Alpha (Alpha - průhlednost)
white = (255, 255, 255)
red = (255, 0, 0)

#          x   y
#          0   1
CarPos = [50, 100]
PrevCarPos = CarPos.copy()
CarRadius = 30
CarObdelnik = None

#               levy horni roh - x,y               sirka a vyska
prekazka1 = [display_width // 2, display_height // 2, 50, 100]
prekazka2 = [display_width // 3, display_height // 2, 50, 100]

seznam_prekazek = [prekazka1, prekazka2]

hodiny = pygame.time.Clock()
fps = 20


def draw_car(c, s, r):
    #  x**2 + y**2 - R**2 = 0
    ovlivneny_obdelnik = pygame.draw.circle(screen, c, s, r, 0)
    pygame.draw.line(screen, white, s, (s[0], s[1] + r), 3)
    return ovlivneny_obdelnik


running = True
while running:
    # do fronty událostí pygame.event.get() se ukládají všechny události v průběhu jednoho frame
    for event in pygame.event.get():  # události -> start, quit, zmáčknutí klávesy, klik myší, pohyb myší, ...
        if event.type == pygame.QUIT:
            running = False

    # hodnoty stisknutých kláves v tomto aktuálnim okamžiku
    vsechny_klavesy = pygame.key.get_pressed()  # {K_a:True, K_b:False, K_c:True, .....}

    if vsechny_klavesy[pygame.K_a]:
        CarPos[0] = CarPos[0] - 5
    if vsechny_klavesy[pygame.K_d]:
        CarPos[0] = CarPos[0] + 5
    if vsechny_klavesy[pygame.K_w]:
        CarPos[1] = CarPos[1] - 5
    if vsechny_klavesy[pygame.K_s]:
        CarPos[1] = CarPos[1] + 5

    if vsechny_klavesy[pygame.K_r]:
        CarPos = [0, 0]

    screen.fill(white)
    CarObdelnik = draw_car(black, CarPos, CarRadius)
    pygame.draw.rect(screen, black, prekazka1, 10)
    pygame.draw.rect(screen, black, prekazka2, 0)

    index_kolize = CarObdelnik.collidelist(seznam_prekazek)
    if index_kolize > -1:  # narazil jsem do prekazky
        # CarPos = PrevCarPos.copy()
        prekazka_narazena = seznam_prekazek[index_kolize]
        CarPos[0] = prekazka_narazena[0] + prekazka_narazena[2] // 2
        CarPos[1] = prekazka_narazena[1] + prekazka_narazena[3] // 2
        draw_car(red, CarPos, CarRadius)

    PrevCarPos = CarPos.copy()

    hodiny.tick(fps)
    pygame.display.update()

pygame.quit()
