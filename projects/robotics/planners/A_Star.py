#!/usr/bin/env python3
'''https://www.youtube.com/watch?v=ob4faIum4kQ'''

from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        # if the parent exists, record state relative to parent
        if parent:
            self.path = parent.path[:]  #makes a copy of the contents of a list into the target list
            self.path.append(value)     # Also store the new value
            self.start = parent.start
            self.goal = parent.goal
        else:
            # record new state
            self.path = [value]
            self.start = start
            self.goal = goal

    def getDist(self):
        pass

    def createChildren(self):
        pass

class State_String(State):
    '''subclass of State'''
    def __init__(self, value, parent, start=0, goal=0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.getDist()

    def getDist(self):
        # if at the goal, you're there!
        if self.value == self.goal:
            return 0
        dist=0
        for i in range(0,len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def createChildren(self):
        if not self.children:
            print(F"Creating Children{self}")
            for i in range(0,len(self.goal)-1):
                val = self.value
                # creates a new arrangement of the letters
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []  # so that we don't visit children 2x and get in a loop
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        startState = State_String(self.start,0,self.start,self.goal)

        # creates ID for a child
        count = 0
        self.priorityQueue.put((0,count,startState)) # put a tuple into the queue

        # while the path is empty and the priorityQueue has a size
        while(not self.path and self.priorityQueue.qsize()):
            print(F"self.path: {self.path} and pqsize: {self.priorityQueue.qsize()}")
            closestChild = self.priorityQueue.get()[2]  # this is the reference to the startState index of the top-priority tuple
            closestChild.createChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                print(F"Checking child {child} out of {len(closestChild.children)}")
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:  # if the child dist = 0 then this is the goal
                        self.path = child.path
                        print(F"Goal Found! {self.path}")
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print(F"Goal of {self.goal} is not possible")
        return self.path

if __name__ == "__main__":
    start1 = "abcabcabcabc"
    goal1 = "aaaabbbbcccc"
    print("Starting...")
    a = AStar_Solver(start1, goal1)
    a.solve()
    for i in range(0,len(a.path)):
        print(F"{i} {a.path[i]}")



