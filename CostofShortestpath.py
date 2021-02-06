# Python program for Dijkstra's  
# single source shortest 
# path algorithm. The program 
# is for adjacency matrix 
# representation of the graph 
  
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    # A utility function to find the  
    # vertex with minimum dist value, from 
    # the set of vertices still in queue 
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist array,pick one which 
        # has min value and is till in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
  
    # Function to print shortest path 
    # from source to j 
    # using parent array 
    def printPath(self, parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1 :  
            print('Shortest Path:\n Source:'+cities[j]+','),
            return
        self.printPath(parent , parent[j]) 
        print ("      >>"+cities[j]+",")
          
  
    # A utility function to print 
    # the constructed distance 
    # array 
    def printSolution(self, dist, parent,src): 
        print("Src-->Dest: \t\t Cost from Source to Destination ") 
        for i in range(0, len(dist)):
            print("%s --> %s \t\t Cost:%d" % (cities[src], cities[i], dist[i])),
            Path=self.printPath(parent,i)
            if ( i < 6 ):
                print("next Destination:")
            else:
                print("End:")
            #Path=self.printPath(parent,i)
            #print("\n%s --> %s \t\t%d \t\t" % (cities[src], cities[i], dist[i])), 
            #self.printPath(parent,i)
  
  
    '''Function that implements Dijkstra's single source shortest path 
    algorithm for a graph represented using adjacency matrix 
    representation'''
    def dijkstra(self, graph, src): 
  
        row = len(graph) 
        col = len(graph[0]) 
  
        # The output array. dist[i] will hold 
        # the shortest distance from src to i 
        # Initialize all distances as INFINITE  
        dist = [float("Inf")] * row 
  
        #Parent array to store  
        # shortest path tree 
        parent = [-1] * row 
  
        # Distance of source vertex  
        # from itself is always 0 
        dist[src] = 0
      
        # Add all vertices in queue 
        queue = [] 
        for i in range(row): 
            queue.append(i) 
              
        #Find shortest path for all vertices 
        while queue: 
  
            # Pick the minimum dist vertex  
            # from the set of vertices 
            # still in queue 
            u = self.minDistance(dist,queue)  
  
            # remove min element      
            queue.remove(u) 
  
            # Update dist value and parent  
            # index of the adjacent vertices of 
            # the picked vertex. Consider only  
            # those vertices which are still in 
            # queue 
            for i in range(col): 
                '''Update dist[i] only if it is in queue, there is 
                an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of 
                dist[i]'''
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
  
  
        # print the constructed distance array 
        self.printSolution(dist,parent,src) 
  
g= Graph() 
G = [[0, 110, 132, INF, INF, INF, INF],
    [110, 0, INF, 159, INF, INF, 59],
    [132, INF, 0, INF, 89, INF, 120],
    [INF, 159, INF, 0, INF, 98, 108],
    [INF, INF, 89, INF, 0, 68, 102],
    [INF, INF, INF, 98, 68, 0, 92],
    [INF, 59, 120, 108, 102, 92, 0]]


graph = [[0, 110, 132, 0, 0, 0, 0],
    [110, 0, 0, 159, 0, 0, 59],
    [132, 0, 0, 0, 89, 0, 120],
    [0, 159, 0, 0, 0, 98, 108],
    [0, 0, 89, 0, 0, 68, 102],
    [0, 0, 0, 98, 68, 0, 92],
    [0, 59, 120, 108, 102, 92, 0]]

cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
start = 0
no_of_people = 0
dest_cities = []
unique_cities = {}


try:
    start = cities.index(str(input('Enter start city: ')).upper()[0])
    print('Start city is: ', cities[start])

    no_of_people = int(input('Enter the no. of people on the ship: '))
    # print(no_of_people)

    for i in range(0, no_of_people):
        msg = "Enter destination city for person " + str(i) + ": "
        # print(msg)
        dest_cities.append(cities.index(str(input(msg)).upper()[0]))
    print(dest_cities)
except:
    print('Unexpected input!')


#start = cities.index(str(input('Enter start city: ')).upper()[0])
g.dijkstra(graph,start)  
