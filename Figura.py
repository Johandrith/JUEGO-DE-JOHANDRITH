import pygame


class Figura:

    def __init__(self, x, y, simbolo, color, tipo):
        self.x = x
        self.y = y
        self.simbolo = simbolo
        self.color = color
        self.tipo = tipo
        self.seleccionada = False
        self.primer_movimiento = True

    def dibujar(self, pantalla):

        if self.seleccionada:
            pygame.draw.circle(
                pantalla,
                (255, 0, 0),
                (self.x, self.y),
                35,
                3
            )

        fuente = pygame.font.SysFont(
            "Segoe UI Symbol",
            60
        )

        # Blancas con borde negro
        # Negras con borde blanco
        if self.color == (255, 255, 255):
            color_borde = (0, 0, 0)
        else:
            color_borde = (255, 255, 255)

        borde = fuente.render(
            self.simbolo,
            True,
            color_borde
        )

        borde_rect = borde.get_rect()
        borde_rect.center = (self.x, self.y)

        pantalla.blit(borde, (borde_rect.x - 1, borde_rect.y))
        pantalla.blit(borde, (borde_rect.x + 1, borde_rect.y))
        pantalla.blit(borde, (borde_rect.x, borde_rect.y - 1))
        pantalla.blit(borde, (borde_rect.x, borde_rect.y + 1))

        texto = fuente.render(
            self.simbolo,
            True,
            self.color
        )

        rect = texto.get_rect()
        rect.center = (self.x, self.y)

        pantalla.blit(texto, rect)

    def presionada(self, mouse_x, mouse_y):

        return (
            self.x - 40 <= mouse_x <= self.x + 40
            and
            self.y - 40 <= mouse_y <= self.y + 40
        )

    def mover(self, x, y):

        self.x = x
        self.y = y
        self.primer_movimiento = False

    def hay_pieza(self, x, y, piezas):

        for pieza in piezas:
            if pieza.x == x and pieza.y == y:
                return pieza

        return None

    def camino_libre(self, nuevo_x, nuevo_y, piezas):

        dx = 0
        dy = 0

        if nuevo_x > self.x:
            dx = 85
        elif nuevo_x < self.x:
            dx = -85

        if nuevo_y > self.y:
            dy = 85
        elif nuevo_y < self.y:
            dy = -85

        x = self.x + dx
        y = self.y + dy

        while x != nuevo_x or y != nuevo_y:

            if self.hay_pieza(x, y, piezas):
                return False

            x += dx
            y += dy

        return True

    def movimiento_valido(self, nuevo_x, nuevo_y, piezas):

        if nuevo_x == self.x and nuevo_y == self.y:
            return False

        pieza_destino = self.hay_pieza(
            nuevo_x,
            nuevo_y,
            piezas
        )

        # No capturar piezas propias
        if (
            pieza_destino
            and pieza_destino.color == self.color
        ):
            return False

        # ======================
        # PEÓN
        # ======================

        if self.tipo == "peon":

            direccion = -85 if self.simbolo == "♙" else 85

            # Avanzar una casilla
            if (
                nuevo_x == self.x
                and nuevo_y == self.y + direccion
                and pieza_destino is None
            ):
                return True

            # Avanzar dos casillas al inicio
            if (
                self.primer_movimiento
                and nuevo_x == self.x
                and nuevo_y == self.y + direccion * 2
                and pieza_destino is None
                and self.hay_pieza(
                    self.x,
                    self.y + direccion,
                    piezas
                ) is None
            ):
                return True

            # Captura diagonal
            if (
                abs(nuevo_x - self.x) == 85
                and nuevo_y == self.y + direccion
                and pieza_destino is not None
                and pieza_destino.color != self.color
            ):
                return True

            return False

        # ======================
        # TORRE
        # ======================

        elif self.tipo == "torre":

            if (
                nuevo_x != self.x
                and nuevo_y != self.y
            ):
                return False

            return self.camino_libre(
                nuevo_x,
                nuevo_y,
                piezas
            )

        # ======================
        # CABALLO
        # ======================

        elif self.tipo == "caballo":

            dx = abs(nuevo_x - self.x) // 85
            dy = abs(nuevo_y - self.y) // 85

            return (
                (dx == 2 and dy == 1)
                or
                (dx == 1 and dy == 2)
            )

        # ======================
        # ALFIL
        # ======================

        elif self.tipo == "alfil":

            dx = abs(nuevo_x - self.x)
            dy = abs(nuevo_y - self.y)

            if dx != dy:
                return False

            return self.camino_libre(
                nuevo_x,
                nuevo_y,
                piezas
            )

        # ======================
        # REINA
        # ======================

        elif self.tipo == "reina":

            dx = abs(nuevo_x - self.x)
            dy = abs(nuevo_y - self.y)

            if (
                dx == dy
                or nuevo_x == self.x
                or nuevo_y == self.y
            ):
                return self.camino_libre(
                    nuevo_x,
                    nuevo_y,
                    piezas
                )

            return False

        # ======================
        # REY
        # ======================

        elif self.tipo == "rey":

            dx = abs(nuevo_x - self.x) // 85
            dy = abs(nuevo_y - self.y) // 85

            return dx <= 1 and dy <= 1

        return False