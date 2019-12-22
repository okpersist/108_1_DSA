# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected,  
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
