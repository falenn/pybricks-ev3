
from node import Node

def diag_hueristic(nodeA: Node, nodeB: Node) -> int:
  deltaX = abs(nodeA.x - nodeB.x)
  deltaY = abs(nodeA.y - nodeB.y)

  if(deltaX > deltaY):
    return 14 * deltaY + 10 * (deltaX - deltaY);
  return 14 * deltaX + 10 * (deltaY - deltaX);
