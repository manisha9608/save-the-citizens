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

import numpy as np;

INF = 1000000

def floydWarshall(graph):
    n = len(graph)

    dist = [[] for i in range(n)]


    # Initialize the dist matrix as same as the input graph∂
    for i in range(n):
        for j in range(n):
            dist[i].append(graph[i][j])

    # Calculate shortest path distance for each pair
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

    # Shortest distance for every pair of vertex.
    print('Shortest Distance between every pair of vertex:-')
    for i in range(n):
        for j in range(n):
            if dist[i][j]==INF:
                print ("%7s" % ("INF"),end=' ')
            else:
                print ("%7s" % (dist[i][j]),end=' ')
        print()

    return dist

def main():
    G = [[0, 110, 132, INF, INF, INF, INF],
    [110, 0, INF, 159, INF, INF, 59],
    [132, INF, 0, INF, 89, INF, 120],
    [INF, 159, INF, 0, INF, 98, 108],
    [INF, INF, 89, INF, 0, 68, 102],
    [INF, INF, INF, 98, 68, 0, 92],
    [INF, 59, 120, 108, 102, 92, 0]]
    # print(G)

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

    reqd_cities = [city for city in dest_cities]
    reqd_cities.extend([start])
    # print(reqd_cities)
    # print(dest_cities)
    unique_cities = sorted(set(reqd_cities))
    print(unique_cities)
    dist = floydWarshall(G)

    # new_g =




main()