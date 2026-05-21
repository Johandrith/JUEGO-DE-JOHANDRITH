import pygame

def dibujar_peon(pantalla, x, y, color):

    # cabeza
    pygame.draw.circle(pantalla, color, (x, y), 10)

    # cuello
    pygame.draw.rect(pantalla, color, (x - 5, y + 8, 10, 8))

    # cuerpo
    pygame.draw.rect(pantalla, color, (x - 10, y + 16, 20, 30))

    # base
    pygame.draw.rect(pantalla, color, (x - 18, y + 46, 36, 8))