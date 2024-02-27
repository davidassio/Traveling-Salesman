import numpy as np
import time

def read_city_distances(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_cities = int(lines[0])
    distance_matrix = np.array([list(map(float, line.split())) for line in lines[1:]])
    return num_cities, distance_matrix

def tsp_branch_and_bound(dist_matrix):
    num_cities = len(dist_matrix)
    best_tour = None
    best_tour_length = float('inf')

    def backtrack(tour, tour_length, lower_bound, time_limit = 600):
        nonlocal best_tour, best_tour_length

        if time.time() - start_time > time_limit:  # Check if time limit exceeded
            return

        if len(tour) == num_cities:
            tour_length += dist_matrix[tour[-1], tour[0]]
            if tour_length < best_tour_length:
                best_tour = tour[:]
                best_tour_length = tour_length
        else:
            current_city = tour[-1]
            for city in range(num_cities):
                if city not in tour:
                    new_tour = tour + [city]
                    new_tour_length = tour_length + dist_matrix[current_city, city]
                    new_lower_bound = lower_bound + nearest_neighbor(dist_matrix, new_tour)
                    if new_lower_bound < best_tour_length:
                        backtrack(new_tour, new_tour_length, new_lower_bound)

    def nearest_neighbor(dist_matrix, tour):
        unvisited_cities = [city for city in range(len(dist_matrix)) if city not in tour]
        if not unvisited_cities:
            return dist_matrix[tour[-1], tour[0]]
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: dist_matrix[current_city, city])
        return dist_matrix[current_city, nearest_city]

    for start_city in range(num_cities):
        backtrack([start_city], 0, nearest_neighbor(dist_matrix, [start_city]))

    return best_tour, best_tour_length

if __name__ == "__main__":
    filename = "input_file"  # Replace with input file
    num_cities, distance_matrix = read_city_distances(filename)

    start_time = time.time()
    tour, tour_length = tsp_branch_and_bound(distance_matrix)
    end_time = time.time()
    execution_time = end_time - start_time
    tour_length = round(tour_length, 4)

    print("Optimal Tour:", tour)
    print("Tour Length:", tour_length)
    print("Execution Time (seconds):", execution_time)
