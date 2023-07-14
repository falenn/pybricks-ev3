#!/usr/bin/env python
from astar import AStar
from nodeset import NodeSet
from node import Node
from numpy import *




def createField() -> NodeSet:
  """
    field is a matrix, where 1 is starting node, 
    2 is the goal and -1 are walls (unwalkable nodes)
  """
  field = array([[1,0,0,0,0,0,0,0],
                 [0,-1,0,0,0,-1,0,0],
                 [0,-1,0,0,0,-1,0,0],
                 [0,0,0,-1,0,-1,0,0],
                 [0,0,0,-1,0,0,0,0],
                 [0,0,0,-1,0,0,0,0],
                 [0,0,0,0,0,-1,0,2],
                 [0,0,0,0,0,-1,0,0]
                 ])
  'shape and make a matrix'
  field = reshape(field,(8,8))
  print(field)

  nset = NodeSet() 

  for i in range(len(field)):
        for j in range(len(field[i])):
           n = Node(i,j)
           n.set_cost = field[i][j]
           nset.add(n)
  return nset;


if __name__ == "__main__":
  'create an instance of the AStar planner'
  field = createField()
  print(field)
  #ast = AStar(createField())
