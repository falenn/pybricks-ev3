from nodeset import NodeSet

class Node:

  def __init__(self, x:int = 0, y:int = 0):
    self.x = x
    self.y = y
    self.cost:int = 0
    self.parent:Node = None
    """calculated cost from start node to this node
       The algorithm sets neighbor node gcosts based on currentNode gcost + hueristic to the neighbor node
       This is a step-wise cost assignment.
    """
    self.gcost:int = 0
    'estimated hueristic cost from this node to the goal'
    self.hcost:int = 0
    'stores whether walkable or not'
    self.walkable = True
    'Set of neighouring nodes'
    self.neighbours:NodeSet = NodeSet()

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y 

  def get_cost(self) -> int:
    return self.cost

  def set_cost(self,cost:int):
    self.cost = cost

  def set_hcost(self,cost:int):
    '@TODO could calculate on creation if goal node is provided along with hueristic module'
    self.hcost = cost

  def get_hcost(self) -> int:
    return self.hcost

  def set_gcost(self,cost:int):
    '@TODO is this summed when discovered, perhaps this is "cost?"'
    self.gcost = cost
  
  def get_gcost(self) -> int:
    return self.gcost

  def set_parent(self, parent):
    self.parent = parent

  def get_parent(self):
    return self.parent
  
  def get_neighbours(self) -> NodeSet:
    return self.neighbours

  def add_neighbour(self, node):
    self.neighbours.add(node)

  def is_walkable(self) -> bool:
    return self.walkable

  'Equality check methods'
  def __eq__(self, other):
    if self.x == other.x and \
       self.y == other.y:
       return True
    return False

  def __ne__(self, other):
    if self.x != other.x or \
       self.y != other.y:
       return True
    return False

