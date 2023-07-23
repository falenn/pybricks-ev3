from hueristic import diag_hueristic as diag
from node import Node
from nodeset import NodeSet

class AStar():
  """
  f(n) = g(n) + h(n)
  g(n): the cost of the path from the start point to any vertex n
  h(n): the hueristic estimated cost from vertex n to the goal
  """
  
  def __init__(self,openset: NodeSet):
    'nodes that have calculated costs'
    self.openset = NodeSet()
    'nodes that have no calculated cost'
    self.closedset = NodeSet()

  def findpath(self,startNode:Node, endNode:Node):
    """A Star algo, starting with startNode, finding
       lowest cost to endNode"""
    self.openset.add(startNode)
    
    while(self.openset.size() > 0):
      self.openset.sort()
      currentNode:Node = self.openset.pop_front()
      self.closedset.add(currentNode)

      'Finally, find the goal, trace path to parent'
      if(currentNode == endNode):
        path = NodeSet()
        while currentNode != startNode:
          self.path.add(currentNode)
          currentNode = currentNode.get_parent()
        return path
      else:
        'iterate over all the neighbours'
        '@TODO - what does walkable mean?'
        for neighborNode in currentNode.get_neighbours():
          if not neighborNode.is_walkable() or self.closedset.contains(neighborNode):
              continue

          'continue here is an option to exit otherwise.'
          '@TODO review logic'
          """NeighbourNode gCost assignment is stepwise, from current node gcost + hueristic"""
          cost = currentNode.get_cost() + diag(currentNode, neighborNode)
          if cost < neighborNode.get_gcost() or not self.openset.contains(neighborNode):
            neighborNode.set_gcost(cost)
            neighborNode.set_hcost(diag(neighborNode,endNode))
            neighborNode.set_parent(currentNode)
            if not self.openset.contains(neighborNode):
              self.openset.add(neighborNode)
    return None
  
