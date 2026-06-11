import pygame

def tablero(screen, tamaño):

    # Colores clásicos del ajedrez
    BLANCO = (255, 255, 255)
    MARRON = (70, 70, 70)
    for fila in range(8):
        for columna in range(8):

            # Alternar colores de las casillas
            if (fila + columna) % 2 == 0:
                color = BLANCO
            else:
                color = MARRON

            pygame.draw.rect(
                screen,
                color,
                (columna * tamaño, fila * tamaño, tamaño, tamaño)
            )