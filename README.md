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


Instructions:

Click and drag your mouse around the grid to make a cube Alive or Dead.
Use the "enter" key to move on to the next generation (You can hold this button to keep going).
Similarly, you can use the "h" key to move on to the next generation as fast as possible (Using the "enter" key has a limit to the speed, although it's very slow when dealing with bigger grids. The "h" key completely removes the speed limit.)
Use the "s" key to save the board to a file named "save.board" in the "saves" folder. Inside this folder, you'll find some boards that I've added into the program by default, so feel free to mess around with those and see what they do. Be aware that closing the program doesn't automatically save your board. Remember to save your progress!
If you want to import a different file, simply delete the "save.board" file (or rename it if you want to save it for later) and name the file you want to import to "save.board"


Additionally, you can generate a blank board by running the "saveboardgen.py" file, which will prompt for x and y coordinates of the blank board and create the board in the "generated_boards" folder.
