import pygame, sys
from pygame.locals import *
from Tablero import *

def main():
    pygame.init()

    ANCHO = 680
    ALTO = 680

    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mi primer juego en Python")

    clock = pygame.time.Clock()

    # colores para mi ventana
    BLANCO = (255, 255, 255)
    MARRON = (139, 69, 19)
    NEGRO = (0, 0, 0)

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLANCO)

        font = pygame.font.SysFont("Arial", 30)

        mitexto = font.render("Hola Mundo!", True, MARRON)

        text_rect = mitexto.get_rect()
        text_rect.center = (ANCHO // 2, ALTO // 2)
        screen.blit(mitexto, text_rect)

        tablero(screen, 85)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()