#!/usr/bin/python3


from CS312Graph import *
from UnsortedArray import *
import time


class NetworkRoutingSolver:
    def __init__( self ):
        self.heap = False
        self.unArray = False
        self.queue = None
        self.visitedArray = []
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex

        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE

        path_edges = []
        total_length = 0
        startNode = self.network.nodes[self.source]
        # edges_left = 3
        # while edges_left > 0:
        #     edge = node.neighbors[2]
        #     path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
        #     total_length += edge.length
        #     node = edge.dest
        #     edges_left -= 1
        currentNodeItem = self.queue.getItem(self.network.nodes[self.dest])
        prevNodeItem = currentNodeItem
        currentNodeItem = currentNodeItem.prev
        while (currentNodeItem != None):
            print(currentNodeItem.node)
            for edge in currentNodeItem.node.neighbors:
                if edge.dest.node_id == prevNodeItem.node.node_id:
                    path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
            prevNodeItem = currentNodeItem
            currentNodeItem = currentNodeItem.prev
        print(total_length)
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap ):
        self.source = srcIndex
        self.heap = use_heap
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)

        self.djikstras(self.source)
        # print("djikstras is done")
        # for item in self.queue.array:
        #    print("{}: {}".format(item.node.node_id, item.dist))
        t2 = time.time()
        return (t2-t1)

    def makeQueue(self):
        if not self.heap:
            unArr = UnsortedArray()
            for node in self.network.getNodes():
                unArr.array.append(ArrayItem(node, 10000, None))
            unArr.array[self.source].dist = 0
            return unArr

    def deleteMin(self):
        if not self.heap:
            smallestNum = 100000
            smallestIndex = 0
            for i in range(len(self.queue.array)):
                if self.queue.array[i].dist < smallestNum and self.queue.array[i].dist != -1 \
                        and self.queue.array[i].visited is False:
                    smallestIndex = i
                    smallestNum = self.queue.array[i].dist

            self.queue.array[smallestIndex].visited = True
            return self.queue.array[smallestIndex]

    def djikstras(self, srcIndex):
        self.queue = self.makeQueue()
        done = False
        while done is False:
            done = True
            for item in self.queue.array:
                if item.visited is False:
                    done = False
            currentItem = self.deleteMin()
            # print(currentItem.visited)
            for edge in currentItem.node.neighbors:
            #    print("{} to {}: {}".format(edge.length, edge.dest.node_id, edge.dest.loc))
                neighborAsItem = self.queue.getItem(edge.dest)
                if neighborAsItem is None:
                    continue
                if neighborAsItem.dist > edge.length + currentItem.dist:
            #        print("{} > {}".format(self.queue.getItem(edge.dest).dist, edge.length + currentItem.dist))
            #        print("it worked lol")
                    neighborAsItem.dist = edge.length + currentItem.dist
                    neighborAsItem.prev = currentItem
            self.result.append(currentItem)


        # for item in queue.array:
        #     print(item.node)
        # print(srcIndex)
        # for node in self.network.getNodes():
        #     print("NODE: {}".format(node.node_id))
        #     for neighbor in node.neighbors:
        #         print("{} to {}: {}".format(neighbor.length, neighbor.dest.node_id, neighbor.dest.loc))
        # print(self.dest)
