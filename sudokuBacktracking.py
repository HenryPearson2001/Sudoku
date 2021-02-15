# program which solves sudoku via backtracking methods
# will only solve 9x9 sudokus
import time
# class which will store data about a square to reduce time required for checks
class square:

    # created properties when initialised to make them instances of the object not class
    def __init__(self):
        # value of the square
        self.value = " "
        # the arrays storing the squares in the vicinity of the square
        self.rowSquares = [" "," "," "," "," "," "," "," "]
        self.columnSquares = [" "," "," "," "," "," "," "," "]
        self.squareSquares = [" "," "," "," "," "," "," "," "]
        

# class to represent the whole of a sudoku board
class sudokuGrid:
    squares = []

    def __init__(self):
        # populate the array of squares with the square object
        for i in range(0,81):
            self.squares.append(square())
        # now fill in the correct values for the squares rows and columns
        for i in range(0,81):
            # the location of the square within the grid
            rowPosition =  i // 9
            columnPosition = i % 9
            count = 0
            # add all squares in that row
            for j in range(rowPosition*9,rowPosition*9 + 9):
                if self.squares[j] != self.squares[i]:
                    self.squares[i].rowSquares[count] = self.squares[j]
                    count += 1
            count = 0
            # add all squares in that column
            for j in range(0,9):
                if self.squares[j*9 + columnPosition] != self.squares[i]:
                    self.squares[i].columnSquares[count] = self.squares[j*9 + columnPosition]
                    count += 1
            # tuple to store the top left corner of square 3x3 grid square exists is
            topLeftSquare = ((rowPosition // 3) * 3,(columnPosition // 3) * 3)
            count = 0
            # add all squares in that square - iterate through the 3x3 subgrid
            for j in range(topLeftSquare[0], topLeftSquare[0] + 3):
                for z in range(topLeftSquare[1], topLeftSquare[1] + 3):
                    if self.squares[j * 9 + z] != self.squares[i]:
                        self.squares[i].squareSquares[count] = self.squares[j * 9 + z]
                        count += 1


    # method which will output a visulisation of the board
    def outputGrid(self):
        # output the first 3 rows
        for i in range(0,3):
            gridLine = ''
            for j in range(0,3):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            gridLine = gridLine + (' | ')
            for j in range(3,6):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            gridLine = gridLine + (' | ')
            for j in range(6,9):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            print(gridLine)
        # separate the grid rows into squares
        print('---------- ----------- ----------')
        # output the next 3 rows
        for i in range(3,6):
            gridLine = ''
            for j in range(0,3):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            gridLine = gridLine + (' | ')
            for j in range(3,6):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            gridLine = gridLine + (' | ')
            for j in range(6,9):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            print(gridLine)
        # separate the grid rows into squares
        print('---------- ----------- ----------')
        # output the final 3 rows
        for i in range(6,9):
            gridLine = ''
            for j in range(0,3):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            gridLine = gridLine + (' | ')
            for j in range(3,6):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            gridLine = gridLine + (' | ')
            for j in range(6,9):
                gridLine = gridLine + ('[' + self.squares[i*9 + j].value + ']')
            print(gridLine)


    # checks if an input is valid and returns true if so, otherwise returns false.
    # takes coordinates and value as input (coordinates in format (row,column)
    def checkIfValid(self,move,moveValue):
        # get the square at which the move is being made
        squarePosition = move[0]*9 + move[1] 
        square = self.squares[squarePosition]
        # if the square is already occupied, the move is invalid
        if square.value != " ":
            return False
        # otherwise check rows, columns and squares
        else:
            # iterate through all neighboring squares, if any of them contain the same value the move is invalid
            for i in range(0,8):
                if square.rowSquares[i].value == moveValue or square.columnSquares[i].value == moveValue or square.squareSquares[i].value == moveValue:
                    return False
            # otherwise the move is valid
            return True

    # method which updates the grid when a move is made
    def addInput(self,move,moveValue):
        # get the square at which the move is being made
        squarePosition = move[0]*9 + move[1]
        square = self.squares[squarePosition]
        # update the value of the square
        square.value = moveValue

    # method which goes through grid and will return a completed sodoku, solving puzzle via backtracking methods, and will output the completed sudoku
    def backtrackSolver(self,depth):
        # the case where the gird is filled and hence sudoku solved
        if depth == 81:
            self.outputGrid()
            print("\n")
        # the case where the grid space is already occupied (part of the puzzle)
        elif self.squares[depth].value != " ":

            # go to the next square and apply the backtracking algorithm
            self.backtrackSolver(depth + 1)
        # otherwise run the algorithm normally on square
        else:
            for i in range(1,10):
                # the location of the square within the grid
                rowPosition =  depth // 9
                columnPosition = depth % 9
                # if a valid move, enter the move and then apply algoithm to next position
                if self.checkIfValid((rowPosition,columnPosition),str(i)):
                    self.squares[depth].value = str(i)
                    self.backtrackSolver(depth + 1)
                    self.squares[depth].value = " "

    # method which takes inputs to make sudoku puzzle
    def makeGrid(self):
        building = True
        while building:
            self.outputGrid()
            rowPosition = int(input("Please enter the row number of the next entry in the sudoku (1 is top, 9 is bottom).\n"))
            columnPosition = int(input("Please enter the column number of the next entry in the sudoku (1 is left, 9 is right).\n"))
            value = input("Please enter the value you would like to input there (-1 quits inputs).\n")
            move = (rowPosition - 1,columnPosition - 1)
            if value == "-1":
                building = False
            else:
                self.addInput(move,value)
            
                
    
grid = sudokuGrid()
grid.makeGrid()
print("\n")
start = time.time()
grid.backtrackSolver(0)
end = time.time()
print("Completed in ", (end - start), " seconds.")
