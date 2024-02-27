import math
import itertools
import random
import numpy as np
import time

# Function to read the distance matrix and the number of cities from a file
def read_distance_matrix(file_path):
    with open(file_path, 'r') as file:
        num_cities = int(file.readline())  # Read the number of cities
        distances = np.loadtxt(file, dtype=float)  # Read the matrix
    return num_cities, distances


# Read the distance matrix from the file
file_path = "input_file"  # Update with the correct file path
num_cities, distances_matrix = read_distance_matrix(file_path) #get the cities and the distances matrix


#calculates the distance given a path and a distance matrix
def calculate_distance(path:list,distances:list):
    distance = 0
    pathLength: int = num_cities
    place = 0
    while place < pathLength - 1:
        x = path[place]
        y = path[place+1]
        distance = distance + distances[x][y]
        place += 1
    start = path[0]
    last = path[pathLength -1]
    distance = distance + distances[start][last]

    return distance


#This method does a hill climb search using random iterations of the cities, it calculates a distance checks if it is better than best distance, if it is better the function goes through another iteration, if not the function returns the local best distance and path
def hillClimbSearch(cities, distances):
    bestDistance = float('inf')
    bestPath = []
    checkedPaths =[[]]
    currentPath = list(range(0, cities))
    currentDistance = 0.0
    i = 0
    while currentDistance <= bestDistance and i <= math.factorial(cities):
        randomPath = currentPath.copy()
        random.shuffle(randomPath)
        if randomPath not in checkedPaths:
            currentDistance = calculate_distance(randomPath, distances)
            checkedPaths.append(randomPath.copy())
            if currentDistance < bestDistance:
                bestDistance = currentDistance
                bestPath = randomPath.copy()
        i += 1
    return bestPath, bestDistance

start_time = time.time()
bp, bd = hillClimbSearch(num_cities,distances_matrix)
end_time = time.time()
execution_time = end_time - start_time
print("Best Path Found: ",bp)
print("Best Cost Found: ",bd)
print("Time Taken: ", execution_time)