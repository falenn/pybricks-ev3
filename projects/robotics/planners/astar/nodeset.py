import node as Node

class NodeSet:
    def __init__(self):
      self.children = []

    def add(self, node: Node):
      """ Add a node """
      self.children.append(node)

    def size(self):
      """Return number of nodes"""
      return self.children.count

    def sort(self):
      """ sort the list by node cost.
          Uses a lambda function to sort in-place,
          uses reverse=False to sort in ascending order - 
          lowest cost at index 0."""
      self.children.sort(key=lambda x: x.cost, reverse=False)

    def pop_front(self):
      """Return first node"""
      return self.children[0]

    def contains(self,node:Node)-> bool:
      """@TODO implement search through list"""
      return False

    