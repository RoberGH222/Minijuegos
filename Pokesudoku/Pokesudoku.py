import pygame
import sys

crossword_board = [
    ['', 'Eveelution', 'Flying', 'Monotype'],
    ['Water', '', '', ''],
    ['Fire', '', '', ''],
    ['Electric', '', '', ''],
]

# Definir las posibles respuestas para cada celda
possible_answers = {
    (1, 1): {'VAPOREON'},
    (2, 1): {'GYARADOS'},
    (3, 1): {'SQUIRTLE', 'WARTORTLE', 'BLASTOISE', 'PSYDUCK', 'GOLDUCK', 'POLIWAG', 'POLIWHIRL', 'SEEL', 'KRABBY', 'KINGLER', 'HORSEA', 'SEADRA', 'GOLDEEN', 'SEAKING', 'STARYU', 'MAGIKARP'},
    (1, 2): {'FLAREON'},
    (2, 2): {'MOLTRES', 'CHARIZARD'},
    (3, 2): {'CHARMANDER', 'CHARMELEON', 'VULPIX', 'NINETALES', 'GROWLITHE', 'ARCANINE', 'PONYTA', 'RAPIDASH', 'MAGMAR', 'FLAREON'},
    (1, 3): {'JOLTEON'},
    (2, 3): {'ZAPDOS'},
    (3, 3): {'JOLTEON', 'PIKACHU', 'RAICHU', 'VOLTORB', 'ELECTRODE', 'ELECTABUZZ'},
    # Añade las posibles respuestas para las otras celdas aquí
    # Ejemplo: (columna, fila): {'respuesta1', 'respuesta2', 'respuesta3'}
}

# Variable para rastrear si el juego ha terminado
game_finished = False

# Tamaño de la pantalla
WIDTH, HEIGHT = 800, 800

# Tamaño de cada celda
CELL_SIZE = WIDTH // 4

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("POKESUDOKU :)")

# Función para manejar el reinicio del juego
def restart_game():
    global crossword_board
    global game_finished
    global possible_answers
    # Reiniciar el tablero del crucigrama y el estado del juego
    # Definir los Pokémons para el crucigrama
    crossword_board = [
        ['', 'Eveelution', 'Flying', 'Monotype'],
        ['Water', '', '', ''],
        ['Fire', '', '', ''],
        ['Electric', '', '', ''],
    ]

    # Definir las posibles respuestas para cada celda
    possible_answers = {
        (1, 1): {'VAPOREON'},
        (2, 1): {'GYARADOS'},
        (3, 1): {'SQUIRTLE', 'WARTORTLE', 'BLASTOISE', 'PSYDUCK', 'GOLDUCK', 'POLIWAG', 'POLIWHIRL', 'SEEL', 'KRABBY', 'KINGLER', 'HORSEA', 'SEADRA', 'GOLDEEN', 'SEAKING', 'STARYU', 'MAGIKARP'},
        (1, 2): {'FLAREON'},
        (2, 2): {'MOLTRES', 'CHARIZARD'},
        (3, 2): {'CHARMANDER', 'CHARMELEON', 'VULPIX', 'NINETALES', 'GROWLITHE', 'ARCANINE', 'PONYTA', 'RAPIDASH', 'MAGMAR', 'FLAREON'},
        (1, 3): {'JOLTEON'},
        (2, 3): {'ZAPDOS'},
        (3, 3): {'JOLTEON', 'PIKACHU', 'RAICHU', 'VOLTORB', 'ELECTRODE', 'ELECTABUZZ'},
        # Añade las posibles respuestas para las otras celdas aquí
        # Ejemplo: (columna, fila): {'respuesta1', 'respuesta2', 'respuesta3'}
    }

    # Variable para rastrear si el juego ha terminado
    game_finished = False

# Función para mostrar el crucigrama
def draw_board():
    screen.fill(WHITE)
    for y, row in enumerate(crossword_board):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if cell:
                font = pygame.font.Font(None, 24)
                text = font.render(cell, True, BLACK)
                text_rect = text.get_rect(center=(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

# Función para verificar la respuesta del usuario
def check_answer():
    
    if current_cell in possible_answers:
        user_input = crossword_board[current_cell[1]][current_cell[0]].upper()
        if user_input not in possible_answers[current_cell]:
            crossword_board[current_cell[1]][current_cell[0]] = 'ERROR'



# Función para mostrar la ventana de felicitaciones
def show_congratulations():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("¡Felicidades! Has completado el crucigrama.", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    wait_for_click()  # Esperar a que el usuario haga clic para cerrar la ventana

# Función para mostrar la ventana de reintentar
def show_retry_button():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 28)
    text = font.render("No has completado el crucigrama. Haz clic para reintentar.", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verificar si el clic está dentro de los límites del botón
                if text_rect.collidepoint(mouse_x, mouse_y):
                    restart_game()  # Reiniciar el juego al hacer clic en el botón
                    waiting = False  # Salir del bucle de espera

# Función para esperar a que el usuario haga clic para cerrar la ventana
def wait_for_click():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Bucle principal del juego
running = True
current_cell = None  # Variable para rastrear la celda seleccionada
current_input = ""  # Variable para almacenar la entrada del usuario
game_started = False  # Variable para indicar si el juego ha comenzado

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del clic del mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Calcular la celda seleccionada
            cell_x, cell_y = mouse_x // CELL_SIZE, mouse_y // CELL_SIZE
            # Verificar si la celda seleccionada no es una etiqueta
            if crossword_board[cell_y][cell_x] == '':
                current_cell = (cell_x, cell_y)
                current_input = ""  # Limpiar la entrada actual al seleccionar una celda
        elif event.type == pygame.KEYDOWN:
            if current_cell and event.key == pygame.K_RETURN:
                # Al presionar Enter, guardar la entrada actual en la celda seleccionada
                crossword_board[current_cell[1]][current_cell[0]] = current_input.upper()
                check_answer()  # Verificar si la respuesta es correcta o incorrecta
                current_cell = None
            elif current_cell and event.key == pygame.K_BACKSPACE:
                # Manejar retroceso para eliminar caracteres de la entrada actual
                current_input = current_input[:-1]
            elif current_cell and len(current_input) < 10 and event.unicode.isalpha():
                # Limitar la longitud de la entrada a 10 caracteres
                current_input += event.unicode
        

    draw_board()
    
    # Mostrar la entrada actual en la pantalla si hay una celda seleccionada
    if current_cell is not None:
        font = pygame.font.Font(None, 24)
        text = font.render(current_input, True, BLACK)
        text_rect = text.get_rect(center=(current_cell[0] * CELL_SIZE + CELL_SIZE // 2, current_cell[1] * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(text, text_rect)

    # Lógica para comprobar si todas las celdas están rellenadas y sin errores
    all_cells_filled = all(all(row) for row in crossword_board[1:])

    if all_cells_filled:
        check_answer()  # Verificar las respuestas solo si no hay errores
        game_finished = True

    all_cells_filled = all(all(row) for row in crossword_board[1:])
    any_error_present = any('ERROR' in row for row in crossword_board[1:])

    # Lógica para comprobar si el juego ha terminado y mostrar la ventana correspondiente
    if game_finished:
        if all_cells_filled and not any_error_present:
            show_congratulations()  # Mostrar la ventana de felicitaciones
        else:
            show_retry_button()  # Mostrar la ventana de reintentar

    # Iniciar el juego si no ha comenzado
    if not game_started:
        restart_game()
        game_started = True

    pygame.display.flip()

pygame.quit()
sys.exit()

