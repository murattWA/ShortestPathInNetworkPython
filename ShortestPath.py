import sys


class ShortestPathAlgorithim:
    def __init__(current):  # our base class for our program
        current.NO_PARENT = -1  # if the current node has no parent set its parent = -1
import sys


class ShortestPathAlgorithim:
    def __init__(current):  # our base class for our program
        current.NO_PARENT = -1  # if the current node has no parent set its parent = -1
        current.path = []  # nodes in the shortest_path path
        current.allLengths = []  # list data structure of shortest_path distance, keep insertion order

    # use Dijkstra’s shortest_path Path Algorithm, Time O(n^2)  n is number of nodes, Dijkstra’s finds the shortest
    def shortestPath(current, adjacency_matrix, start, final):
        n = len(adjacency_matrix[0])
        shortest_path = {}  # shortest distance from source node to all vertices
        already_visited = {}  # boolean value true or false if a node has already been visited
        previous = {}  # saves the previous vertex in the shortest path
        # initialize variables defined above
        for v in range(0, n, 1):
            shortest_path[v] = sys.maxsize  # initially set all vertices' paths other than itself to maximum size
            already_visited[v] = False  # no nodes have been visited at this point, so it is set to false initially
        shortest_path[start] = 0  # shortest path from the starting node is 0 initially
        previous[start] = current.NO_PARENT  # set the parent of the starting node to no parent initially
        # Visit each vertex and initialize the values
        for i in range(1, n, 1):
            old = -1  # initialize the old vertex to -1
            min = sys.maxsize  # set the initial shortest path to max size
            # Visit each path and find the shortest path
            for v in range(0, n, 1):
                if already_visited[v] == False and shortest_path[v] < min:
                    old = v  # save the vertex associated with the shortest path
                    min = shortest_path[v]  # save the shortest path
            if old == -1:  # if there is no shortest distance return -1
                return
            already_visited[old] = True
            for v in range(0, n, 1):
                dist = adjacency_matrix[old][v]  
                if dist > 0 and ((min + dist) < shortest_path[v]):
                    previous[v] = old  # set the shortest path's previous node
                    shortest_path[v] = min + dist  # add the weights of the edges and the vertices to the list
        current.allLengths.append(shortest_path[final])  # add the shortest to the list

# Test code to make sure it is working correctly with our given adjacency matrix from example G1.1
adjacency_matrix = [
    [0, 5, 0, 5, 0, 0, 10],
    [5, 0, 0, 20, 10, 0, 0],
    [0, 0, 0, 0, 15, 1, 0],
    [5, 20, 0, 0, 0, 0, 0],
    [0, 10, 15, 0, 0, 30, 0],
    [0, 0, 1, 0, 30, 0, 25],
    [10, 0, 0, 0, 0, 25, 0]
]
start = 6
final = 0
myobj = ShortestPathAlgorithim()
myobj.shortestPath(adjacency_matrix, start, final)
print("shortest_path distance: " + str(myobj.allLengths[0]))
