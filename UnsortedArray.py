

class UnsortedArray:
    def __init__(self):
        self.array = []
        pass

    def getItem(self, nodeToGet):
        for item in self.array:
            if item.node == nodeToGet:
                return item
        return None

class ArrayItem:
    def __init__(self, node, dist, prev):
        self.visited = False
        self.node = node
        self.dist = dist
        self.prev = prev
