import sys
import math
import puzzle
import search


def isSquareRoot(n):
    return int(math.sqrt(n))**2 == n


def main():
    n = 8
    if len(sys.argv) == 2 and isSquareRoot(int(sys.argv[1]) + 1):
        n = int(sys.argv[1])

    initMode = input("\nWelcome to Bertie Woosters " + str(n) + "-puzzle solver.\n" +
                     "Type '1' to use a default puzzle, or '2' to enter your own puzzle, or '3' to generate random puzzle.\n")
    print("----------------------------------------\n")

    p = puzzle.Puzzle(int(math.sqrt(n+1)))

    if initMode == '1':
        p.deffault()
    elif initMode == '2':
        p.setPuzzle()
    elif initMode == '3':
        p.randomPuzzle()
    else:
        sys.exit(0)

    print("This is the puzzle:")
    p.showPuzzle()
    print("----------------------------------------")

    print("\nEnter your choice of algorithm:\n 1. Uniform Cost Search.\n 2. A* with the Misplaced Tile heuristic.\n"
          " 3. A* with the Manhattan distance heuristic.")
    mode = input()
    print("----------------------------------------\n")

    s = search.Search(p)
    goal = s.run(mode)

    print("----------------------------------------\n")
    if goal is not None:
        print("\n To solve this problem the search algorithm expanded a total of " + str(s.numOfNodes) + " nodes.")
        print(" The maximum number of nodes in the queue at any one time was " + str(s.maxQueueSize))
        print(" The depth of the goal node was " + str(s.depth))
    else:
        print("\n Can not find the goal!")


if __name__ == "__main__":
    main()