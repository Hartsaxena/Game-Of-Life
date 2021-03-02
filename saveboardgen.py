from pathlib import Path
import os

os.chdir(Path(__file__).parent.absolute())

def create_board(x, y):
    boardrow = [0 for i in range(x)]
    return [boardrow for i in range(y)]

def main():
    while True:
        newx = input("Input the x axis: (the amount of numbers in a row)\n")
        newy = input("Input the y axis: (the amount of rows)\n")
        try:
            newx = int(newx)
            newy = int(newy)
        except ValueError:
            print ("Sorry, but one of the numbers you entered isn't valid.")
            print ("Please try again.")
        else:
            break
    newboard = create_board(newx, newy)
    os.makedirs("generated_boards", exist_ok=True)
    os.chdir("generated_boards")
    finalnum = "OVER_REACHED"
    for num in range(1, 9999):
        if "save" + str(num) + ".board" not in os.listdir():
            finalnum = num
            break
    with open("save" + str(finalnum) + ".board", 'w') as savefile:
        for row in newboard:
            for num in row:
                savefile.write(str(num))
            savefile.write("\n")
    print (f"Succesfully saved the board in the file:\nsave{finalnum}.board\n\nRename the file to \"save.board\" and place it into your \"saves\" folder.")


if __name__ == "__main__":
    while True:
        main()
