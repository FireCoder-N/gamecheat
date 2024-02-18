#######################################
# Game: Pythagorea (HORIS INTERNATIONAL LIMITED)
# Objective: Draw a straight line on a 6x6 grid
# Level: any
# Description: 
#       This script is utilized as a helper for the Pythagorea game, where players tackle geometric challenges on a 6x6 grid.
#       The game involves solving puzzles that require drawing lines on the grid.
#       Although geometric intuition is the primary skill required to solve the puzzles, algebraic techniques can be employed to help the user find solutions to the presented problems.
#
# About:
#       The script takes a linear equation 'y = ax + b' as input and identifies the grid points intersected by the corresponding line.
#       Points satisfying specific conditions (x, y within the grid range of 0 to 6 and having fractional parts 0, 0.25, 0.50, 0.75) are printed.
#       The user has to calculate the needed slope and y-intercept themselves. (i.e. given a perpendicular line, two points, etc.)
#       The a and b values are entered as fractions (e.g. 1/2), exactly as the equation is derived by the user.
#
# Ideas for further improvement:
#
#######################################

from fractions import Fraction

while True:
    y = input('y = ')
    if y == '':
        break
    a = ''
    for c in y:
        if c == 'x':
            break
        a += c

    a = float(Fraction(a))
    y = y[len(str(a))+1:]
    b = float(Fraction(y))

    for xi in [x / 100.0 for x in range(0, 625, 25)]:
        yi = a*xi + b
        if (yi*100)%100 in [0, 25, 50, 75] and yi<6:
            print(f"({xi}, {yi})")
