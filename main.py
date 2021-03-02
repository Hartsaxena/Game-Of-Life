from copy import deepcopy
from pathlib import Path
import os
import pygame
import sys


os.chdir(Path(__file__).parent.absolute())
pygame.init()

if os.path.exists("saves/save.board"): # Loads the saved board, if one exists.
    loadingdata = []
    with open("saves/save.board", 'r') as savefile:
        rawloadingdata = [line.rstrip("\n") for line in savefile.readlines()]
        for row in range(len(rawloadingdata)):
            loadingdata.append([])
            for char in rawloadingdata[row]:
                loadingdata[row].append(int(char))
        BOARD_X = len(loadingdata[0])
        BOARD_Y = len(loadingdata)
        board = deepcopy(loadingdata)

    boardrow = [0 for i in range(1, BOARD_X + 1)] # We still need to define boardrow, since it's needed for deleting the board.
else:
    BOARD_X = 50
    BOARD_Y = 40

    boardrow = [0 for i in range(1, BOARD_X + 1)]
    board = [deepcopy(boardrow) for i in range(1, BOARD_Y + 1)]

    board[25][20], board[25][21], board[25][22], board[24][22], board[23][21] = 1, 1, 1, 1, 1 # Creates the famous glider

def neighbors(board, pos, influ=False): # pos will be in [row, col]
    selected = board[pos[0]][pos[1]]
    neighboredsquares = [
    [pos[0] - 1, pos[1] - 1],
    [pos[0] - 1, pos[1]],
    [pos[0] - 1, pos[1] + 1],
    [pos[0], pos[1] - 1],
    [pos[0], pos[1] + 1],
    [pos[0] + 1, pos[1] - 1],
    [pos[0] + 1, pos[1]],
    [pos[0] + 1, pos[1] + 1]
    ]
    result = 0
    neighbored = []
    for position in neighboredsquares:
        if validsquare(board, position):
            if board[position[0]][position[1]] == 1:
                result += 1
    return result

def validsquare(board, pos):
    try:
        test = board[pos[0]][pos[1]]
    except IndexError:
        return False
    else:
        if pos[0] < 0 or pos[1] < 0:
            return False
        return True

def movestep(board):
    # Moves the board forward by a step
    newboard = deepcopy(board)
    for row in range(len(board)):
        for col in range(len(board[0])):
            selected = board[row][col]
            num_neighbors = neighbors(board, [row, col])
            if selected == 1:
                if num_neighbors == 2 or num_neighbors == 3:
                    newboard[row][col] = 1
                else:
                    newboard[row][col] = 0

            elif selected == 0:
                if num_neighbors == 3:
                    newboard[row][col] = 1
                else:
                    newboard[row][col] = 0
    return newboard

def save_board(filepath, board): # Save a board
    with open(filepath, 'w') as savefile:
        for row in range(len(board)):
            for col in range(len(board[0])):
                savefile.write(str(board[row][col]))
            savefile.write("\n")

def main(board):
    screen = pygame.display.set_mode((BOARD_X * 15 + 5, BOARD_Y * 15 + 5))
    pygame.display.set_caption("John Conway's Game of Life")
    clock = pygame.time.Clock()

    # RGB values of basic colors.
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    scrollcount = 0
    selected = [5, 5, [0, 0]] # Set the selected square to the very first square (0, 0)
    pressinglist = []

    squarelist = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            squarelist.append([col * 15 + 5, row * 15 + 5, [row, col]])

    while True:
        scrollcount += 1
        clock.tick()
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the grid
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 0:
                    pygame.draw.rect(screen, WHITE, (col * 15 + 5, row * 15 + 5, 10, 10))
                else:
                    pygame.draw.rect(screen, RED, (col * 15 + 5, row * 15 + 5, 10, 10))


        keys = pygame.key.get_pressed()

        if scrollcount >= 6 and keys[pygame.K_RETURN]: # scrollcount represents Different speeds (the smaller scrollcount is, the slower the emulation is.)
            board = movestep(board)  # Advances the board by one step
            scrollcount = 0
        if scrollcount >= 3 and keys[pygame.K_SPACE]:
            board = movestep(board)
            scrollcount = 0
        if scrollcount >= 1 and keys[pygame.K_v]:
            board = movestep(board)
            scrollcount = 0
        if keys[pygame.K_h]:
            board = movestep(board)
            scrollcount = 0

        if keys[pygame.K_BACKSPACE]: # Resets the board to completely empty
            board = [deepcopy(boardrow) for i in range(1, BOARD_Y + 1)]

        if keys[pygame.K_s]: # Save the current board
            save_board("saves/save.board", board)

        mouse_pos = pygame.mouse.get_pos()
        for square in squarelist:
            if (mouse_pos[0] < square[0] + 10 and mouse_pos[0] > square[0]) and (mouse_pos[1] > square[1] and mouse_pos[1] > square[1] - 10):
                selected = square

        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]: # Detects if the left mouse button is being pressed
            if selected not in pressinglist:
                if board[selected[2][0]][selected[2][1]] == 1:
                    board[selected[2][0]][selected[2][1]] = 0
                else:
                    board[selected[2][0]][selected[2][1]] = 1
                pressinglist.append(selected)

        elif mouse_buttons[0] == False:
            pressinglist = []


        pygame.display.update()

def consolemain(board):
    while True:
        for row in board:
            print (row)
        input()
        board = movestep(board)


if __name__ == "__main__":
    main(board)
