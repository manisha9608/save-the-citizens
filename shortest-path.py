# Artificial and Computational Intelligence Assignment 4
#Identify the correct uninformed search strategy for the given Assignment.
#Things to follow
    #1.	Use appropriate data structures to represent the graph and the path using python libraries
    #2.	Provide proper documentation
    #3.	Find the path and print it
#Coding begins here



#1.	Define the agent environment in the following block
    #PEAS environment, Initial data structures to define the graph and variable declarations


#2.	Define a formula that Checks for existence of path
    #Function for checking for the  path


#3.	Implementation of search technique for finding the path
    #Code block 1


#4.	Calling main function
    #Function call to the search technique


#5.	The agent should provide the following output
    #5.1.	Whether a path exists
    #Function to find the existence of path


    #5.2.	The path that covers required vertices in the graph
    #Function that prints the path covering required vertices using appropriate uninformed search


    #5.3.	Print the total number of vertices (areas) visited by the agent in finding the path
    #Execute code to print the number of vertices travelled to cover the path. (using appropriate uninformed search)



from collections import defaultdict 

#Class to represent a graph 
class Graph: 
    
    cost = 0
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


    # Function to get shortest path 
    # from source to j 
    # using parent array 
    def addPath(self, parent, j): 
        #Base Case : If j is source 
        if parent[j] == -1 :  
            return
        self.addPath(parent , parent[j])
        if parent[j] != -1:
            sol_path.append(j)
            
    # Function to get cost 
    # from source to j 
    # using dist array
    def addCost(self,dist,j):
        g.cost = g.cost + dist[j]

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
        #print(dist)
        mini = float("Inf")
        min_dest = -1
        
        #Choose the nearest Destination to the source
        for i in dest_cities:
            if dist[i]<mini:
                mini = dist[i]
                min_dest = i
        
        if min_dest == -1:
            return -1
        else:
            dest_cities.remove(min_dest)
            self.addCost(dist,min_dest)
            self.addPath(parent,min_dest)
            return min_dest

g= Graph() 
#G = [[0, 110, 132, INF, INF, INF, INF],
#    [110, 0, INF, 159, INF, INF, 59],
#    [132, INF, 0, INF, 89, INF, 120],
#    [INF, 159, INF, 0, INF, 98, 108],
#    [INF, INF, 89, INF, 0, 68, 102],
#    [INF, INF, INF, 98, 68, 0, 92],
#    [INF, 59, 120, 108, 102, 92, 0]]
#

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
sol_path = []


try:
    start = cities.index(str(input('Enter start city: ')).upper()[0])
    print('Start city is: ', cities[start])
    sol_path.append(start)
    no_of_people = int(input('Enter the no. of people on the ship: '))
    # print(no_of_people)

    for i in range(0, no_of_people):
        msg = "Enter destination city for person " + str(i) + ": "
        # print(msg)
        dest_cities.append(cities.index(str(input(msg)).upper()[0]))
    #print(dest_cities)
except:
    print('Unexpected input!')

while dest_cities:
    if start != -1:
        start=g.dijkstra(graph,start)
    else:
        break
    
if start != -1:
    print("The Shortest path is ")
    for i in sol_path: print(" ", cities[i], end = " ") 
    print("\nCost of Path is ", g.cost)
else:
    print("Path does not exist")
