import state
import queue


class Search:
    def __init__(self, puzzle):
        self.root = state.State(puzzle)
        self.depth = 0
        self.numOfNodes = 0
        self.maxQueueSize = 0


    def run(self, mode):
        nodes = queue.PriorityQueue()
        self.root.setHeuristic(mode)
        nodes.put(self.root)
        expanded = list()

        print("Expanding state: ", end = "")
        while True:
            if nodes.empty():
                return None

            self.maxQueueSize = max(self.maxQueueSize, nodes.qsize())

            node = nodes.get()
            self.numOfNodes += 1

            if node is self.root:
                print("Expanding state: ")
            else:
                print("The best state to expand with a g(n) = " + str(node.depth) + " and h(n) = " + str(node.heuristic) + " is: ")

            node.state.showPuzzle()

            if node.goalTest() == True:
                self.depth = node.depth
                print("\n\nGoal!!")
                return node

            print("Expanding this node...\n")

            expanded.append(node.state.puzzle)
            children = node.expand()
            while not children.empty():
                child = children.get()
                if child.state.puzzle not in expanded:
                    child.setHeuristic(mode)
                    nodes.put(child)