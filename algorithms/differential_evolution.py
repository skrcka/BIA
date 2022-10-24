import random
import numpy as np

import static_data
import func_file
import show_3D_graph


CR = 0.6

def de(func, dimension, popsize, generations, scaling_vector):
    all_points = []
    population = generate_first_population(func, popsize, dimension)
    all_points.append(population)

    num_generation = 0
    while num_generation < generations:
        new_population = []
        for i in range(popsize):
            parent = random.sample(range(popsize), 3)

            parents = [population[x] for x in parent]
            mutation_v = mutation_pop(parents, dimension, scaling_vector, func)

            child = []
            for index in range(dimension):
                r = random.uniform(0, 1)
                if r <= CR:
                    child.append(mutation_v[index])
                else:
                    child.append(population[i][index])
            child.append(func_file.return_value_function(child, func))

            if child[2] < population[i][2]:
                new_population.append(child)
            else:
                new_population.append(population[i])
        all_points.append(new_population)
        population = new_population
        num_generation += 1

    return population, all_points


def generate_first_population(func, popSize, dimension):
    population = []
    for i in range(popSize):
        gen_point = list(np.random.uniform(static_data.get_min_range(func), static_data.get_max_range(func), dimension))
        gen_point.append(func_file.return_value_function(gen_point, func))
        population.append(gen_point)
    return population


def mutation_pop(parents, dimension, scaling_vector, func):
    mutation_v = []
    for j in range(dimension):
        mutation_v.append(np.clip(parents[0][j] + scaling_vector * (parents[1][j]) - parents[2][j], static_data.get_min_range(func), static_data.get_max_range(func)))
    mutation_v.append(func_file.return_value_function(mutation_v, func))
    return mutation_v
