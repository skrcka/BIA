import numpy as np
import random
import copy

import func_file
import static_data


C1 = 2
C2 = 2

def PSO(func, dim, popSize, iteration, vmax):
    population = generate_first_population(func, popSize, dim)
    gBest = find_best_in_list(population, func)
    new_population = []
    all_points = []

    points = [copy.copy(point[0]) for point in population]
    for point in points:
        point.append(func_file.return_value_function(point, func))
    all_points.append(points)
    
    for i in range(iteration):

        for j in population:
            new_velocity = []
            new_point = []
            for x in range(dim):
                # point j = [[x,y], [velocity_x, velocity_y], [pBest_x,pBest_y]]
                new_velocity.append(j[1][x] + (C1 * random.uniform(0, 1) * (j[2][x] - j[0][x])) + (
                        C2 * random.uniform(0, 1) * (gBest[x] - j[0][x])))
                new_point.append(j[0][x] + new_velocity[x])


            for m in range(dim):
                if new_velocity[m] > vmax or new_velocity[m] < -vmax:
                    new_velocity[m] = new_velocity[m] / 20

            for i in range(dim):
                if new_point[i] > static_data.get_max_range(func):
                    new_point[i] = random.uniform(static_data.get_min_range(func), static_data.get_max_range(func))
                if new_point[i] < static_data.get_min_range(func):
                    new_point[i] = random.uniform(static_data.get_min_range(func), static_data.get_max_range(func))

            if func_file.return_value_function(new_point, func) < func_file.return_value_function(j[2], func):
                pBest = new_point
            else:
                pBest = j[2]
            if func_file.return_value_function(pBest, func) < func_file.return_value_function(gBest, func):
                gBest = pBest

            new_population.append([new_point, new_velocity, pBest])


        # for graph
        points = [copy.copy(point[2]) for point in new_population]
        for point in points:
            point.append(func_file.return_value_function(point, func))
        all_points.append(points)

        population = new_population
        new_population = []
    return all_points

def generate_first_population(func, popSize, dimension):
    population = []
    for i in range(0, popSize):
        gen_point = list(np.random.uniform(static_data.get_min_range(func), static_data.get_max_range(func), dimension))
        velocity = list(np.random.uniform(-1, 1, dimension))
        population.append([gen_point, velocity, gen_point])
    return population

def find_best_in_list(population, func):
    min_value = func_file.return_value_function(population[0][0], func)
    leader = population[0]
    for point in population:
        if func_file.return_value_function(point[0], func) < min_value:
            leader = point
            min_value = func_file.return_value_function(point[0], func)
    return leader[0]
