Pacman.py holds the logic for the FDSE take home assignment.
The script takes in one argument of an input file which contains the four inputs as described in the assignment. 

Requirements:
Python 2.7 

To run the code, type 'python Pacman.py input.txt' from a Mac OS X terminal.


Assumptions:

* Inputs board_dimension, initial_position and walls will only take the first two integers as input, rest of the input on that line will be ignored.
* Valid movement instructions are N, E, S, W only, any other character will be ignored.
* If a wall and the Pacman's initial position have the same coordinates, Pacman takes precedence over the wall. That wall will be ignored.
* Wall with coordinates that are out of board range will be ignored.
