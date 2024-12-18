import pygame

# --- Constants ---
GRID_SIZE = 200
CELL_SIZE = 6
WIDTH = GRID_SIZE * CELL_SIZE 
HEIGHT = GRID_SIZE * CELL_SIZE -200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ANT_COLOR = (255, 0, 0)
BUTTON_COLOR = (0, 150, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

# --- Ant Directions ---
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Langton's Ant")

# --- Fonts ---
font_title = pygame.font.SysFont(None, 48)
font_text = pygame.font.SysFont(None, 24)
font_button = pygame.font.SysFont(None, 36)

# --- Explanation Text ---
explanation_text = [
    "Langton's Ant is a cellular automaton with simple rules:",
    "1. At a white square, turn 90° right, change the square to black, move forward one unit.",
    "",
    "2. At a black square, turn 90° left, change the square to white, move forward one unit.",
    "",
    "Initially chaotic, the ant eventually builds a repeating 'highway' pattern."
]

# --- Button Dimensions and Position---
button_rect = pygame.Rect(WIDTH // 4, HEIGHT - 80, WIDTH // 2, 60)

# --- Functions ---
def draw_text(text, font, color, surface, x, y, max_width):
    """Draws text with word wrapping."""
    words = text.split()
    space = font.size(' ')[0]  # Width of a space.
    
    current_line = []
    current_line_width = 0

    for word in words:
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        
        if current_line_width + word_width >= max_width:
            # Render the current line and start a new one.
            draw_words = " ".join(current_line)
            line_surface = font.render(draw_words, True, color)
            surface.blit(line_surface, (x, y))
            
            y += word_height  # Move to the next line.
            current_line = [word]
            current_line_width = word_width
        else:
            # Add the word to the current line.
            current_line.append(word)
            current_line_width += word_width + space

    # Render the last line.
    if current_line:
        draw_words = " ".join(current_line)
        line_surface = font.render(draw_words, True, color)
        surface.blit(line_surface, (x, y))

def draw_explanation_screen():
    """Draws the explanation screen."""
    screen.fill(WHITE)
    title_surface = font_title.render("Langton's Ant", True, TEXT_COLOR)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(title_surface, title_rect)

    x = 30  # X-coordinate for text (with some margin)
    y_offset = 120
    max_width = WIDTH - 2 * x  # Available width for text.

    for line in explanation_text:
        draw_text(line, font_text, TEXT_COLOR, screen, x, y_offset, max_width)
        y_offset += font_text.get_linesize() + 5  # Adjust line spacing.

    # Draw the button.
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    button_text_surface = font_button.render("Simulate", True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text_surface.get_rect(center=button_rect.center)
    screen.blit(button_text_surface, button_text_rect)
    
def initialize_simulation():
    """Sets up the grid and ant for the simulation."""
    global ant_x, ant_y, ant_direction, grid
    # Reinitialize the grid
    grid = [[WHITE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Place the ant in the center, facing up
    ant_x = GRID_SIZE // 2
    ant_y = GRID_SIZE // 2
    ant_direction = UP

def update_ant():
    """Updates the ant's position and direction."""
    global ant_x, ant_y, ant_direction
    if grid[ant_y][ant_x] == WHITE:
        ant_direction = (ant_direction + 1) % 4
        grid[ant_y][ant_x] = BLACK
    else:
        ant_direction = (ant_direction - 1) % 4
        grid[ant_y][ant_x] = WHITE

    if ant_direction == UP:
        ant_y -= 1
    elif ant_direction == RIGHT:
        ant_x += 1
    elif ant_direction == DOWN:
        ant_y += 1
    elif ant_direction == LEFT:
        ant_x -= 1

    ant_x %= GRID_SIZE
    ant_y %= GRID_SIZE

def draw_grid():
    """Draws the grid and the ant."""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, ANT_COLOR, (ant_x * CELL_SIZE, ant_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# --- Game Loop ---
clock = pygame.time.Clock()
running = True
show_explanation = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_explanation and button_rect.collidepoint(event.pos):
                show_explanation = False
                initialize_simulation()
    if show_explanation:
        draw_explanation_screen()
    else:
        update_ant()
        draw_grid()
    pygame.display.flip()
    clock.tick(600)  # Slower frame rate on explanation screen
pygame.quit()