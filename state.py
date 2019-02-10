import copy
import queue


class State:
    def __init__(self, puzzle, parent = None):
        self.state = puzzle
        self.parent = parent
        self.heuristic = 0
        self.cost = 0
        if parent is None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1


    def __lt__(self, other):
        try:
            return self.cost < other.cost
        except AttributeError:
            return NotImplemented


    def expand(self):
        children = queue.Queue()
        for i_ in range(1, 5):
            node = copy.deepcopy(self.state)
            node.move(i_)
            if node.blank is not self.state.blank:
                children.put(State(node, self))

        return children


    def goalTest(self):
        return self.state.goalTest()


    def setHeuristic(self, mode):
        if mode == '1':
            self.heuristic = 0
        elif mode == '2':
            self.heuristic = self.state.misplacedTile()
        elif mode == '3':
            self.heuristic = self.state.manhattanDistance()

        self.cost = self.depth + self.heuristic