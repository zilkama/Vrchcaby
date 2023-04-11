import pygame

# konstanty velikosti okna a desky
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
BOARD_SIZE = 500

# barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CHECKER_SIZE = 40
CHECKER_OFFSET = 10

CELL_SIZE = 50
STONE_RADIUS = 20

stones = [
    #kameny hrace 1
    (0, 0), (2, 0), (4, 0), (6, 0), (11, 0), (16, 0),
    #kameny hrace 2
    (0,5), (2,5), (4,5), (6,5), (11,5), (16,5),

    (8, 0),(10, 0),(13, 0),(15, 0),(8, 5),(10, 5),(13, 5),(15,5),
    (1, 1),(3, 1),(5, 1),(7, 1),(10, 1),(12, 1),(14, 1),(16, 1),
    (1, 4),(3, 4),(5, 4),(7, 4),(10, 4),(12, 4),(14, 4),(16, 4)

]

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Vrchcaby")

#board = pygame.Surface((BOARD_SIZE, BOARD_SIZE))
#board.fill(GREY)

#line_width = 4
#pygame.draw.line(board, BLACK, (BOARD_SIZE // 2, 0), (BOARD_SIZE // 2, BOARD_SIZE), line_width)

#player1_checkers = []
#player2_checkers = []

def draw_board():
    for y in range(2):
        for x in range(12):
            pygame.draw.rect(window, WHITE, (x * CELL_SIZE, y * CELL_SIZE * 6, CELL_SIZE, CELL_SIZE * 3))
            pygame.draw.rect(window, BLACK, (x * CELL_SIZE, (y+1) * CELL_SIZE * 3, CELL_SIZE, CELL_SIZE * 3))

    for stone in stones:
        x, y = stone
        color = RED if y < 3 else BLACK
        pygame.draw.circle(window, color, (int(x*CELL_SIZE+CELL_SIZE/2), int(y*CELL_SIZE+CELL_SIZE/2)), STONE_RADIUS)

    pygame.display.update()

#for i in range(3):
 #   for j in range(4):
  #      if (i+j) % 2 == 0:
   #         x = j * (BOARD_SIZE // 8) + (BOARD_SIZE // 16)
    #        y = i * (BOARD_SIZE // 4) + (BOARD_SIZE // 8)

     #       player1_checkers.append((x,y))
      #      player2_checkers.append((BOARD_SIZE - x - CHECKER_SIZE, BOARD_SIZE - y - CHECKER_SIZE))

#def draw_checkers(color, position):
 #   x, y = position
  #  pygame.draw.rect(board, color, (x, y, CHECKER_SIZE, CHECKER_SIZE))

#for checker in player1_checkers:
 #   draw_checkers(RED, checker)

#for checker in player2_checkers:
 #   draw_checkers(BLUE, checker)



#window.blit(board, (WINDOW_WIDTH // 2 - BOARD_SIZE // 2, WINDOW_HEIGHT // 2 - BOARD_SIZE // 2))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_board()


pygame.quit()

