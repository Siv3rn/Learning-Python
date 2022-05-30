# Python3 program to print DFS traversal
# from a given  graph
from collections import defaultdict
 
# This class represents a directed graph using
# adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self, v, visited,a):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if a not in visited:
                self.DFSUtil(neighbour, visited,a)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v,a):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited,a)
 

# Driver code
 

# Create a graph given
# in the above diagram

# This code is contributed by Neelam Yadav
# me(sivern) is contributed the stopping point


a = Graph()

a.addEdge (1,2)
a.addEdge (1,10)
a.addEdge (10,11)
a.addEdge (11,12)
a.addEdge (12,13)
a.addEdge (13,14)
a.addEdge (14,15)
a.addEdge (15,16)
a.addEdge (16,17)
a.addEdge (17,18)
a.addEdge (2,3)
a.addEdge (3,4)
a.addEdge (4,5)
a.addEdge (5,6)
a.addEdge (6,7)
a.addEdge (7,8)
a.addEdge (8,19)
a.addEdge (19,20)
a.addEdge (20,21)
a.addEdge (21,22)
a.addEdge (8,9)


a.DFS(1,9)