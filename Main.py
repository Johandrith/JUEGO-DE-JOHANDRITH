import pygame
import sys
from pygame.locals import *
from Tablero import *
from Figura import *

def main():
    pygame.init()

    ANCHO = 680
    ALTO = 820

    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("AJEDREZ EN PYTHON")

    clock = pygame.time.Clock()

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

    piezas = []

    for i in range(8):
        piezas.append(Figura(42 + i * 85, 127, "♟", NEGRO, "peon"))

    piezas.append(Figura(42, 42, "♜", NEGRO, "torre"))
    piezas.append(Figura(127, 42, "♞", NEGRO, "caballo"))
    piezas.append(Figura(212, 42, "♝", NEGRO, "alfil"))
    piezas.append(Figura(297, 42, "♛", NEGRO, "reina"))
    piezas.append(Figura(382, 42, "♚", NEGRO, "rey"))
    piezas.append(Figura(467, 42, "♝", NEGRO, "alfil"))
    piezas.append(Figura(552, 42, "♞", NEGRO, "caballo"))
    piezas.append(Figura(637, 42, "♜", NEGRO, "torre"))

    for i in range(8):
        piezas.append(Figura(42 + i * 85, 552, "♙", BLANCO, "peon"))

    piezas.append(Figura(42, 637, "♖", BLANCO, "torre"))
    piezas.append(Figura(127, 637, "♘", BLANCO, "caballo"))
    piezas.append(Figura(212, 637, "♗", BLANCO, "alfil"))
    piezas.append(Figura(297, 637, "♕", BLANCO, "reina"))
    piezas.append(Figura(382, 637, "♔", BLANCO, "rey"))
    piezas.append(Figura(467, 637, "♗", BLANCO, "alfil"))
    piezas.append(Figura(552, 637, "♘", BLANCO, "caballo"))
    piezas.append(Figura(637, 637, "♖", BLANCO, "torre"))

    pieza_seleccionada = None
    movimientos = 0
    turno_blancas = True

    capturadas_blancas = []
    capturadas_negras = []

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_y > 680:
                    continue

                if pieza_seleccionada:

                    columna = mouse_x // 85
                    fila = mouse_y // 85

                    nuevo_x = columna * 85 + 42
                    nuevo_y = fila * 85 + 42

                    if pieza_seleccionada.movimiento_valido(
                        nuevo_x,
                        nuevo_y,
                        piezas
                    ):

                        captura_realizada = False

                        for pieza in piezas[:]:

                            if (
                                pieza.x == nuevo_x
                                and pieza.y == nuevo_y
                                and pieza != pieza_seleccionada
                            ):

                                if pieza.color != pieza_seleccionada.color:

                                    if pieza_seleccionada.color == BLANCO:
                                        capturadas_blancas.append(pieza.simbolo)
                                    else:
                                        capturadas_negras.append(pieza.simbolo)

                                    piezas.remove(pieza)
                                    captura_realizada = True
                                    break

                        if (
                            captura_realizada
                            or not any(
                                p.x == nuevo_x and p.y == nuevo_y
                                for p in piezas
                                if p != pieza_seleccionada
                            )
                        ):

                            pieza_seleccionada.mover(
                                nuevo_x,
                                nuevo_y
                            )

                            movimientos += 1
                            turno_blancas = not turno_blancas

                    pieza_seleccionada.seleccionada = False
                    pieza_seleccionada = None

                else:

                    for pieza in piezas:

                        if pieza.presionada(mouse_x, mouse_y):

                            if turno_blancas and pieza.color != BLANCO:
                                continue

                            if not turno_blancas and pieza.color != NEGRO:
                                continue

                            pieza.seleccionada = True
                            pieza_seleccionada = pieza
                            break

        screen.fill((0, 0, 0))

        tablero(screen, 85)

        for pieza in piezas:
            pieza.dibujar(screen)

        pygame.draw.rect(
            screen,
            (40, 40, 40),
            (0, 680, 680, 140)
        )

        fuente = pygame.font.SysFont("Arial", 24)

        texto_mov = fuente.render(
            f"Movimientos: {movimientos}",
            True,
            (255, 255, 255)
        )

        turno_texto = "Turno: Blancas" if turno_blancas else "Turno: Negras"

        texto_turno = fuente.render(
            turno_texto,
            True,
            (255, 255, 0)
        )

        screen.blit(texto_mov, (20, 705))
        screen.blit(texto_turno, (350, 705))

        texto_blancas = fuente.render(
            "Blancas capturaron:",
            True,
            (255, 255, 255)
        )

        texto_negras = fuente.render(
            "Negras capturaron:",
            True,
            (255, 255, 255)
        )

        screen.blit(texto_blancas, (20, 740))
        screen.blit(texto_negras, (20, 775))

        fuente_piezas = pygame.font.SysFont("Segoe UI Symbol", 28)

        x = 280
        for simbolo in capturadas_blancas:
            texto = fuente_piezas.render(simbolo, True, (255, 255, 255))
            screen.blit(texto, (x, 740))
            x += 25

        x = 280
        for simbolo in capturadas_negras:
            texto = fuente_piezas.render(simbolo, True, (255, 255, 255))
            screen.blit(texto, (x, 775))
            x += 25

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

