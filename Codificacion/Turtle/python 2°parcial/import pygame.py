import pygame
import random

# Inicializar pygame
pygame.init()

# Configuraciones básicas
ANCHO_VENTANA = 1000
ALTO_VENTANA = 900
TAM_BLOQUE = 30
COLUMNAS = ANCHO_VENTANA // TAM_BLOQUE
FILAS = ALTO_VENTANA // TAM_BLOQUE

# Colores RGB
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
COLORES = [
    (0, 255, 255),   # I
    (0, 0, 255),     # J
    (255, 165, 0),   # L
    (255, 255, 0),   # O
    (0, 255, 0),     # S
    (128, 0, 128),   # T
    (255, 0, 0)      # Z
]

# Figuras de Tetris
FIGURAS = [
    [[1, 1, 1, 1]],                             # I
    [[1, 0, 0], [1, 1, 1]],                     # J
    [[0, 0, 1], [1, 1, 1]],                     # L
    [[1, 1], [1, 1]],                           # O
    [[0, 1, 1], [1, 1, 0]],                     # S
    [[0, 1, 0], [1, 1, 1]],                     # T
    [[1, 1, 0], [0, 1, 1]]                      # Z
]

# Función para rotar una figura
def rotar(figura):
    return [list(fila) for fila in zip(*figura[::-1])]

# Clase para la figura actual
class Pieza:
    def __init__(self):
        self.tipo = random.randint(0, len(FIGURAS) - 1)
        self.figura = FIGURAS[self.tipo]
        self.color = COLORES[self.tipo]
        self.x = COLUMNAS // 2 - len(self.figura[0]) // 2
        self.y = 0

    def mover(self, dx, dy, tablero):
        if not self.colision(dx, dy, tablero, self.figura):
            self.x += dx
            self.y += dy
            return True
        return False

    def rotar_figura(self, tablero):
        nueva = rotar(self.figura)
        if not self.colision(0, 0, tablero, nueva):
            self.figura = nueva

    def colision(self, dx, dy, tablero, figura):
        for y, fila in enumerate(figura):
            for x, celda in enumerate(fila):
                if celda:
                    nx = self.x + x + dx
                    ny = self.y + y + dy
                    if nx < 0 or nx >= COLUMNAS or ny >= FILAS or (ny >= 0 and tablero[ny][nx]):
                        return True
        return False

    def fijar(self, tablero):
        for y, fila in enumerate(self.figura):
            for x, celda in enumerate(fila):
                if celda:
                    tablero[self.y + y][self.x + x] = self.color

# Función para limpiar líneas completas
def limpiar_lineas(tablero):
    nuevas = [fila for fila in tablero if any(c == 0 for c in fila)]
    lineas_borradas = FILAS - len(nuevas)
    for _ in range(lineas_borradas):
        nuevas.insert(0, [0] * COLUMNAS)
    return nuevas

# Crear tablero vacío
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Dibujar el tablero y pieza actual
def dibujar_ventana(ventana, tablero, pieza):
    ventana.fill(NEGRO)
    for y in range(FILAS):
        for x in range(COLUMNAS):
            if tablero[y][x]:
                pygame.draw.rect(ventana, tablero[y][x], (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE))
    for y, fila in enumerate(pieza.figura):
        for x, celda in enumerate(fila):
            if celda:
                pygame.draw.rect(
                    ventana,
                    pieza.color,
                    ((pieza.x + x) * TAM_BLOQUE, (pieza.y + y) * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE)
                )
    for x in range(COLUMNAS):
        pygame.draw.line(ventana, GRIS, (x * TAM_BLOQUE, 0), (x * TAM_BLOQUE, ALTO_VENTANA))
    for y in range(FILAS):
        pygame.draw.line(ventana, GRIS, (0, y * TAM_BLOQUE), (ANCHO_VENTANA, y * TAM_BLOQUE))
    pygame.display.flip()

# Función principal
def main():
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tetris en Python")
    reloj = pygame.time.Clock()
    tablero = crear_tablero()
    pieza = Pieza()
    velocidad = 500  # milisegundos entre caídas
    tiempo = pygame.time.get_ticks()

    ejecutando = True
    while ejecutando:
        reloj.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    pieza.mover(-1, 0, tablero)
                elif evento.key == pygame.K_RIGHT:
                    pieza.mover(1, 0, tablero)
                elif evento.key == pygame.K_DOWN:
                    pieza.mover(0, 1, tablero)
                elif evento.key == pygame.K_UP:
                    pieza.rotar_figura(tablero)

        if pygame.time.get_ticks() - tiempo > velocidad:
            if not pieza.mover(0, 1, tablero):
                pieza.fijar(tablero)
                tablero = limpiar_lineas(tablero)
                pieza = Pieza()
                if pieza.colision(0, 0, tablero, pieza.figura):
                    print("¡Juego terminado!")
                    ejecutando = False
            tiempo = pygame.time.get_ticks()

        dibujar_ventana(ventana, tablero, pieza)

    pygame.quit()

if __name__ == "__main__":
    main()
