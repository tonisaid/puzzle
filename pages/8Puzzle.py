class Node:
    def __init__(self, data, level, value):
        # Initialize the node with the data ,level of the node and the calculated value
        self.data = data
        self.level = level
        self.value = value

    def subNode(self):
        # Create a secondary node from the parent node by moving the empty space in all directions
        x, y = self.findIt(self.data, '_')
        # List of empty space moving directions
        list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        childx = []
        for i in list:
            childN = self.move(self.data, x, y, i[0], i[1])
            if childN is not None:
                child_node = Node(childN, self.level + 1, 0)
                childx.append(child_node)
        return childx

    def move(self, puz, x1, y1, x2, y2):
        # Move the empty space in the appropriate direction
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            puzMo = []
            puzMo = self.transcribe(puz)
            temp = puzMo[x2][y2]
            puzMo[x2][y2] = puzMo[x1][y1]
            puzMo[x1][y1] = temp
            return puzMo
        else:
            return None

    def transcribe(self, root):
        # copy function to create a similar matrix of the given node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def findIt(self, puz, x):
        # Used to find the position of the empty space
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        # Prepare the appropriate size and menus
        self.n = size
        self.open = []
        self.closed = []

    def admission(self):
        # Accepts the puzzle from the user
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def h(self, start, goal):
        # Calculates the difference between the given puzzles
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_ x':
                    temp += 1
        return temp

    def f(self, start, goal):
        # Calculate the value f(x) = h(x) + g(x)
        return self.h(start.data, goal) + start.level

    def process(self):
        # Process Start and Goal Puzzle state
        print("Enter the start state : \n")
        start = self.admission()
        print("Enter the end state : \n")
        goal = self.admission()
        start = Node(start, 0, 0)
        start.value = self.f(start, goal)
        # put the start node in the open list
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("************\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            # if the difference between current and goal node is 0 we have reached the goal node
            if (self.h(cur.data, goal) == 0):
                break
            for i in cur.subNode():
                i.value = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            # sort the open list based on f value
            self.open.sort(key=lambda x: x.value, reverse=False)


puzzle = Puzzle(3)
puzzle.process()



