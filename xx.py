##Dijkstra's - Graph with distances between cities##

neighbours = {
    'A': {'C': 3, 'F': 2},
    'B': {'D': 1, 'E': 2, 'F': 6, 'G': 2},
    'C': {'A': 3, 'D': 4, 'E': 1, 'F': 2},
    'D': {'B': 1, 'C': 4},
    'E': {'B': 2, 'C': 1, 'F': 3},
    'F': {'A': 2, 'B': 6, 'C': 2, 'E': 3, 'G': 5},
    'G': {'B': 2, 'F': 5}
}

#Funtion for Dijkstra's Algorithm
def find_path(start_city, target_city):
    shortestPath = {}
    previousCity = {}
    unexplored = []

    #initialize distances
    for city in unexplored:
        if shortestPath[city] < shortestPath[minCity]:  # moving from one city to other
            minCity = city

    # Remove selected city
    unexplored.remove(minCity)

    for neighbour, distance in neighbours[minCity].items():

        newDistance = shortestPath[minCity] + distance

        # Update shorter distance
        if newDistance < shortestPath[neighbour]:
            shortestPath[neighbour] = newDistance
            previousCity[neighbour] = minCity

    # Build shortest route
    path = []
    current = target_city

    while current != start_city:
        path.append(current)
        current = previousCity[current]

    path.append(start_city)
    path.reverse()
    #Print result
    print("Shortest Distance:", shortestPath[target_city])