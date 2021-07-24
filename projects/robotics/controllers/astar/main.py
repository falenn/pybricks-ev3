''' A-Star algorithm - a shortest-path planning algorithm
f(n) = g(n) + h(n)
n = next node on the path
g(n) = the cost of the path from the start node
h(n) = a heuristic function that estimages the cost
        of the cheepest path from n to the goal

Steps:
1. generate a list of all possible next steps towards 
the goal from the current position

2. Store children in a priority queue based on distance
to the goal, closest first

3. Select closest child and repeat until goal reached
or no more children
'''
