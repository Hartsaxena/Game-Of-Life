# Game-Of-Life
A simulation of John Conway's Game Of Life I made with Pygame. I made this program a while ago (I don't remember when) and I remember being pretty proud of it, since this was the first game I ever made that used Pygame and didn't use ASCII letter graphics.

In order to run the program, you must have Python version 3.7.7 (I haven't tested any other version, so run at your own risk) and pygame version 2.0.1.

Like most programs, run the "main.py" file to execute the program.


The rules of John Conway's Game Of Life are as follows:

There is an infinite grid of cubes (I made a limit to the grid in order to save processing power)
Every cube is in two states: either the cube is Dead or Alive
A cubes "neighbors" are the cubes adjacent to it (all of the squares that share a side or a corner of the square)

Every generation, this happens:
1. If a live square has 2 or 3 neighbors, it will live on.
2. If a live square has more than 3 or less than 2 neighbors, it will die, becoming a Dead square.
3. If a dead square has exactly 3 neighbors, it will become an Alive square.

Be aware that these steps don't have an order to them, the program doesn't evaluate the first condition first, and evaluates all conditions from the original position of the Cubes.
