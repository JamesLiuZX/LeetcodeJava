from random import randint,sample,choice    #choice is more specific than randint and is better suited in the transformations of 1st and 3rd arrays

class Sudoku:
    #initialise a 4x4 2D array with None values
    def __init__(self):      
        self.grid = [[None for i in range(4)]for j in range(4)]
        
    #feed an 16-element array to fill the grid
    def initialiseValues(self,array): 
        for i in range(4):
            for j in range(4):
                self.grid[i][j] = array[i*4 + j]

    def display(self):
        for i in range(4):
            for j in range(4):
                print(self.grid[i][j],end='')  #end = '' to make sure 4 values of the same row is printed on the same line
            print('')

    #swap 1st row with (1st + 1) row or 3rd row with (3rd+1) row        
    def trans1(self):
        row = choice([0,2])         #randomly choose between only these 2 rows (Better alternative to randint in this case)
        temp = self.grid[row]       #swap using a dummy placeholder
        self.grid[row] = self.grid[row+1]
        self.grid[row+1] = temp
        print("Transformation 1 : Swap two rows in the same quadrants")
        s.display()
        
    #for all the rows in the grid, make grid[row][i] swap with grid[row][i+1]
    def trans2(self):
        column = choice([0,2])
        for row in range(4):
            temp = self.grid[row][column]   #swap using a dummy placeholder
            self.grid[row][column] = self.grid[row][column+1]
            self.grid[row][column+1] = temp
        print("Transformation 1 : Swap two columns in the same quadrants")
        s.display()

    #swap 1st row with 3rd then 2nd with 4th
    def trans3(self):
        temp = self.grid[0]         #swap using a dummy placeholder
        self.grid[0] = self.grid[2] 
        self.grid[2] = temp
        temp = self.grid[1]
        self.grid[1] = self.grid[3]
        self.grid[3] = temp
        print("Transformation 3 : Swap top and bottom quadrant rows entirely")
        s.display()
    
    def trans4(self):
        for row in range(4):   #row by row, swap 1st and 3rd value in the row with the 2nd and 4th respectively
            temp = self.grid[row][0]      
            self.grid[row][0] = self.grid[row][2] 
            self.grid[row][2] = temp
            temp = self.grid[row][1]
            self.grid[row][1] = self.grid[row][3]
            self.grid[row][3] = temp            
        print("Transformation 4 : Swaps out the left and right quadrant columns entirely")
        s.display()

    def main(self):
        array = []
        array = sample(range(1,5),2)  #selects 2 unique transformation without dupes
        for i in range(len(array)):
            if array[i] == 1:
                s.trans1()
            elif array[i] == 2:
                s.trans2()
            elif array[i] == 3:
                s.trans3()
            else:
                s.trans4()

s = Sudoku()
values = [4,3,2,1,1,2,4,3,3,4,1,2,2,1,3,4]

s.initialiseValues(values)
s.display()
s.main()
