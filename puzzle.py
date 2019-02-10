import random


class Puzzle:
    def __init__(self, size):
        self.size = size
        self.puzzle = []
        self.goal = []
        self.blank = (0, 0)
        count = 1
        for row in range(0, self.size):
            self.goal.append([])
            self.puzzle.append([])
            for col in range(0, self.size):
                self.goal[row].append(count)
                self.puzzle[row].append(count)
                count += 1
        self.goal[size - 1][size - 1] = 0
        self.puzzle[size - 1][size - 1] = 0


    def deffault(self):
        difficulty = input("Enter the difficulty on a scale from 1 to 6.\n")
        if difficulty == '1':
            self.puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            self.blank = (2, 2)
        elif difficulty == '2':
            print("difficulty: 2")
            self.puzzle = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
            self.blank = (2, 1)
        elif difficulty == '3':
            self.puzzle = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
            self.blank = (0, 2)
        elif difficulty == '4':
            self.puzzle = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
            self.blank = (0, 0)
        elif difficulty == '5':
            self.puzzle = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]
            self.blank = (1, 1)
        elif difficulty == '6':
            self.puzzle = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
            self.blank = (2, 2)


    def setPuzzle(self):
        print("Enter your puzzle, use a zero to represent the blank.")
        numbers = []
        for _i in range(1, self.size + 1):
            if _i % 10 == 1:
                numbers.append(input("Enter the " + str(_i) + "st row, use space or tabs between numbers: ").split())
            elif _i % 10 == 2:
                numbers.append(input("Enter the " + str(_i) + "nd row, use space or tabs between numbers: ").split())
            elif _i % 10 == 3:
                numbers.append(input("Enter the " + str(_i) + "rd row, use space or tabs between numbers: ").split())
            else:
                numbers.append(input("Enter the " + str(_i) + "th row, use space or tabs between numbers: ").split())

        for row in range(0, self.size):
            for col in range(0, self.size):
                self.puzzle[row][col] = int(numbers[row][col])
                if self.puzzle[row][col] == 0:
                    self.blank = (row, col)


    def randomPuzzle(self):
        list = [i for i in range(0, self.size**2)]
        random.shuffle(list)
        count = 0
        for row in range(0, self.size):
            for col in range(0, self.size):
                self.puzzle[row][col] = list[count]
                if list[count] == 0:
                    self.blank = (row, col)
                count += 1


    def goalTest(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.puzzle[row][col] != self.goal[row][col]:
                    return False
        return True


    def showPuzzle(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                print(str(self.puzzle[row][col]).rjust(4) + " ", end = "")
            print("")


    def move(self, m):
        if m == 1:
            self.left()
        if m == 2:
            self.right()
        if m == 3:
            self.up()
        if m == 4:
            self.down()


    def left(self):
        if self.blank[1] == 0:
            return

        row = self.blank[0]
        col = self.blank[1]
        self.puzzle[row][col - 1], self.puzzle[row][col] = self.puzzle[row][col], self.puzzle[row][col - 1]
        self.blank = (self.blank[0], self.blank[1] - 1)


    def right(self):
        if self.blank[1] == self.size - 1:
            return

        row = self.blank[0]
        col = self.blank[1]
        self.puzzle[row][col + 1], self.puzzle[row][col] = self.puzzle[row][col], self.puzzle[row][col + 1]
        self.blank = (self.blank[0], self.blank[1] + 1)


    def up(self):
        if self.blank[0] == 0:
            return

        row = self.blank[0]
        col = self.blank[1]
        self.puzzle[row - 1][col], self.puzzle[row][col] = self.puzzle[row][col], self.puzzle[row - 1][col]
        self.blank = (self.blank[0] - 1, self.blank[1])


    def down(self):
        if self.blank[0] == self.size - 1:
            return

        row = self.blank[0]
        col = self.blank[1]
        self.puzzle[row + 1][col], self.puzzle[row][col] = self.puzzle[row][col], self.puzzle[row + 1][col]
        self.blank = (self.blank[0] + 1, self.blank[1])


    def misplacedTile(self):
        distance = 0
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.puzzle[row][col] != self.goal[row][col] and  self.goal[row][col] != 0:
                    distance += 1
        return distance


    def manhattanDistance(self):
        distance = 0
        for row in range(0, self.size):
            for col in range(0, self.size):
                val = self.puzzle[row][col] - 1
                if val != -1:
                    distance += abs(row - (val // self.size)) + abs(col - (val % self.size))

        return distance