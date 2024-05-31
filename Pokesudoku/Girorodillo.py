import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tamaño de la pantalla
WIDTH, HEIGHT = 850, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Mesa 2D")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Símbolos disponibles
SIMBOLOS = ['Rombo', 'Cuadrado', 'Circulo']

# Clases de personajes
class Personaje:
    def __init__(self, clase):
        self.clase = clase
        self.vida = 10
        self.escudo = 0
        self.variable_izquierda = 0
        self.variable_derecha = 0

# Inicializar personajes para cada jugador
jugador1_personajes = [
    Personaje("Mago"),
    Personaje("Guerrero")
]

jugador2_personajes = [
    Personaje("Mago"),
    Personaje("Cazador")
]

# Inicializar símbolos en las casillas
casillas_jugador1 = [random.choice(SIMBOLOS) for _ in range(5)]
casillas_jugador2 = [random.choice(SIMBOLOS) for _ in range(5)]

def modificar_simbolos():
    global casillas_jugador1, casillas_jugador2
    casillas_jugador1 = [random.choice(SIMBOLOS) for _ in range(5)]
    casillas_jugador2 = [random.choice(SIMBOLOS) for _ in range(5)]

def realizar_tirada(jugador, casillas):
    circulos = casillas.count('Circulo')
    cuadrados = casillas.count('Cuadrado')
    rombos = casillas.count('Rombo')

    # Actualizar el escudo según la cantidad de círculos
    if min(circulos, 5) // 3 + (circulos - 3) >= 0:
        jugador.escudo += min(circulos, 5) // 3 + (circulos - 3)
    

    # Actualizar las variables según la cantidad de cuadrados y rombos
    if jugador.clase == "Mago":
        if min(cuadrados, 5) // 3 + (cuadrados - 3) >= 0:
            jugador.variable_izquierda += min(cuadrados, 5) // 3 + (cuadrados - 3)
        if min(rombos, 5) // 3 + (rombos - 3) >= 0:
            jugador.variable_derecha += min(rombos, 5) // 3 + (rombos - 3)
    elif jugador.clase == "Guerrero" and (min(cuadrados, 5) // 3 + (cuadrados - 3) >= 0 or min(rombos, 5) // 3 + (rombos - 3) >= 0):
        if min(cuadrados, 5) // 3 + (cuadrados - 3) >= 0:
            jugador.variable_izquierda += min(cuadrados, 5) // 3 + (cuadrados - 3)
        if min(rombos, 5) // 3 + (rombos - 3) >= 0:
            jugador.variable_derecha += min(rombos, 5) // 3 + (rombos - 3)
    elif jugador.clase == "Cazador" and (min(cuadrados, 5) // 3 + (cuadrados - 3) >= 0 or min(rombos, 5) // 3 + (rombos - 3) >= 0):
        if min(cuadrados, 5) // 3 + (cuadrados - 3) >= 0:
            jugador.variable_izquierda += min(cuadrados, 5) // 3 + (cuadrados - 3)
        if min(rombos, 5) // 3 + (rombos - 3) >= 0:
            jugador.variable_derecha += min(rombos, 5) // 3 + (rombos - 3)

# Función para dibujar el tablero y los personajes
def dibujar_tablero():
    screen.fill(WHITE)

    # Dibujar jugadores
    pygame.draw.rect(screen, RED, (50, 50, 750, 300))
    pygame.draw.rect(screen, BLUE, (50, 350, 750, 300))

    # Dibujar personajes de jugador 1
    for i, personaje in enumerate(jugador1_personajes):
        pygame.draw.rect(screen, WHITE, (200 * (2 * i + 1), 100, 70, 50))
        font = pygame.font.Font(None, 24)
        texto = font.render(personaje.clase, True, BLACK)
        screen.blit(texto, (200 * (2 * i + 1), 120))

    # Dibujar personajes de jugador 2
    for i, personaje in enumerate(jugador2_personajes):
        pygame.draw.rect(screen, WHITE, (200 * (2 * i + 1), 500, 70, 50))
        font = pygame.font.Font(None, 24)
        texto = font.render(personaje.clase, True, BLACK)
        screen.blit(texto, (200 * (2 * i + 1), 520))

    # Dibujar vidas
    pygame.draw.rect(screen, WHITE, (400, 80, 80, 80))
    pygame.draw.rect(screen, WHITE, (400, 560, 80, 80))
    font = pygame.font.Font(None, 36)
    vida_jugador1 = font.render(f"PV: {jugador1_personajes[0].vida}", True, BLACK)
    vida_jugador2 = font.render(f"PV: {jugador2_personajes[0].vida}", True, BLACK)
    escudo_jugador1 = font.render(f"DEF: {jugador1_personajes[0].escudo}", True, BLACK)
    escudo_jugador2 = font.render(f"DEF: {jugador2_personajes[0].escudo}", True, BLACK)
    var_izq_jugador1 = font.render(f"{jugador1_personajes[0].variable_izquierda}", True, BLACK)
    var_der_jugador1 = font.render(f"{jugador1_personajes[0].variable_derecha}", True, BLACK)
    var_izq_jugador2 = font.render(f"{jugador2_personajes[0].variable_izquierda}", True, BLACK)
    var_der_jugador2 = font.render(f"{jugador2_personajes[0].variable_derecha}", True, BLACK)

    screen.blit(vida_jugador1, (400, 90))
    screen.blit(escudo_jugador1, (400, 120))
    screen.blit(var_izq_jugador1, (200, 150))
    screen.blit(var_der_jugador1, (600, 150))
    screen.blit(vida_jugador2, (400, 600))
    screen.blit(escudo_jugador2, (400, 570))
    screen.blit(var_izq_jugador2, (200, 550))
    screen.blit(var_der_jugador2, (600, 550))

    # Dibujar casillas de jugadores
    for i in range(5):
        pygame.draw.rect(screen, WHITE, (150 + i * 125, 250, 80, 50))
        pygame.draw.rect(screen, WHITE, (150 + i * 125, 400, 80, 50))

        # Seleccionar y mostrar un símbolo al azar
        simbolo_jugador1 = casillas_jugador1[i]
        simbolo_jugador2 = casillas_jugador2[i]

        # Mostrar símbolo en casilla de jugador 1
        font = pygame.font.Font(None, 24)
        texto_jugador1 = font.render(simbolo_jugador1, True, BLACK)
        screen.blit(texto_jugador1, (150 + i * 125, 270))

        # Mostrar símbolo en casilla de jugador 2
        texto_jugador2 = font.render(simbolo_jugador2, True, BLACK)
        screen.blit(texto_jugador2, (150 + i * 125, 420))

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Modificar los símbolos al presionar la tecla "f"
                modificar_simbolos()
                # Realizar la tirada y actualizar variables
                realizar_tirada(jugador1_personajes[0], casillas_jugador1)
                realizar_tirada(jugador2_personajes[0], casillas_jugador2)

    # Dibujar el tablero y los personajes
    dibujar_tablero()

    # Actualizar la pantalla
    pygame.display.flip()


