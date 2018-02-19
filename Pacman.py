"""
Pacman.py holds the logic for the FDSE take home assignment. 
The script takes in one argument of an input file which contains the four inputs as described in the assignment.

Requirement: Python 2.7

To run the code, type 'python Pacman.py input.txt' from a Mac OS X terminal.

Written by: Clara Liu
"""


import sys

#######
# Ensure argument is specified
#######
try:
    arg1 = sys.argv[1]
except IndexError:
    sys.exit("Usage: python Pacman.py <inputFileName>")


#########
# Read the input file and assign variables
#########
try:
    inputFile = open(sys.argv[1], "r")
except IOError:
    sys.exit("Error: input file not found")

# input file must have at least 4 lines (4 inputs)
num_lines = sum(1 for line in inputFile)
if num_lines >= 4:
    inputFile.seek(0)    # move read cursor back to the beginning of file

    # Assign input settings
    board_dimension = inputFile.readline()
    initial_position = inputFile.readline()
    movements = inputFile.readline().strip()
    walls = inputFile.readlines()
else:
    sys.exit("Error: Insufficient number of input")


# Close the input file
inputFile.close()


#############################
# Functions Definition
#############################


#########
# Obtain coordinates from input
#########
def parse_coordinates(dimension):

    individual_dim = dimension.split(" ")

    # coordinates must be a pair of integer
    if len(individual_dim) < 2:
        sys.exit("Error: Incomplete coordinate specified or empty input row")
    else: 
        try:
            cols = int(individual_dim[0])
        except ValueError:
            sys.exit("Error: Coordinate must be an integer")
        
        try:
            rows = int(individual_dim[1])
        except ValueError:
            sys.exit("Error: Coordinate must be an integer")

    return cols, rows


#########
# Helper functions to print board for debugging assistance
#########
def print_board(board):        
    for row in board:
        print " ".join(row)


#########
# Convert between input and board coordinates
# The board is constructed with a list. List index starts at 0 from the top 
# Input coordinates, on the other hand, start at 0 from the bottom left
# This function is to convert between the input and board coordinates
#########
def convert_coordinates(inputX, inputY, boardDimY):
    outputX = inputX
    outputY = boardDimY - inputY - 1
    return outputX, outputY


#########
# Set movement direction coordinate offsets
# Preset coordinate offsets for each valid movement
#########
def coordinate_offsets(movement):
    return {
        'N' : "0 -1",  
        'E' : "1 0",
        'S' : "0 1",
        'W' : "-1 0"
        }.get(movement, "0 0") 


#########
# Move Pacman and collect coins accordingly
#########
def move(x, y, board, coins, movement):
    next_coordinate_x, next_coordinate_y = parse_coordinates(coordinate_offsets(movement))
    next_coordinate_x = x + next_coordinate_x
    next_coordinate_y = y + next_coordinate_y

    # Move only if new coordinate is in range, not a wall 
    if next_coordinate_x in range(board_cols) and next_coordinate_y in range(board_rows):
        if board[next_coordinate_y][next_coordinate_x] != "W":
    
            # Collect coins only if there is still coin
            if board[next_coordinate_y][next_coordinate_x] != " ":
                 coins += 1

            # move pacman coordinate
            board[y][x] = " "
            board[next_coordinate_y][next_coordinate_x] = "P"
            x, y = next_coordinate_x, next_coordinate_y
    return x, y, board, coins



#########
# Setup board with board dimensions
# Create a list and populate with "o" within the range of the list
#########

board_cols, board_rows = parse_coordinates(board_dimension)
board = [["o" for x in range(board_cols)] for y in range(board_rows)]


#########
# Locate initial position of Pacman
#########
initial_position_x, initial_position_y = parse_coordinates(initial_position)
board_pacman_x, board_pacman_y = convert_coordinates(initial_position_x, initial_position_y, board_rows)


if board_pacman_x < 0 or board_pacman_x == board_cols or board_pacman_y < 0:
    sys.exit("Error: Pacman initial position is out of board range")
else:
    if initial_position_y not in range(board_rows) or initial_position_x not in range(board_cols):
        sys.exit("Error: Pacman inital position is out of board range")
    else:
        board[board_pacman_y][board_pacman_x] = "P"


#########
# Setup walls
#########
for wall in walls:
    input_wall_x, input_wall_y = parse_coordinates(wall)

    # setup wall only if wall is not on Pacman and wall is in range
    if (input_wall_y != initial_position_y or input_wall_x != initial_position_x ) \
        and input_wall_y in range(board_rows) and input_wall_x in range(board_cols): 
        board_wall_x, board_wall_y = convert_coordinates(input_wall_x, input_wall_y, board_rows)       
        board[board_wall_y][board_wall_x] = "W"


#########
# Navigation
#########

coins = 0
current_pacman_x, current_pacman_y = board_pacman_x, board_pacman_y

for movement in movements:
    if (movement == "N" or movement == "S" or movement == "E" or movement == "W"): 
        current_pacman_x, current_pacman_y, board, coins = move(current_pacman_x, current_pacman_y, board, coins, movement)


########
# Script Output
#######
output_pacman_x, output_pacman_y = convert_coordinates(current_pacman_x, current_pacman_y, board_rows)
print output_pacman_x, output_pacman_y
print coins
#print print_board(board)
