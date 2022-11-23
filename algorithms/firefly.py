import numpy as np
import random
import copy

import func_file
import static_data
import show_3D_graph

def generate_population(min_, max_, popsize, d):
    population = []
    for i in range(popsize):
        population.append(np.array([random.uniform(min_, max_) for x in range(d)]))
    return population

def distance(a, b):
    return np.linalg.norm(a - b)

def get_best(pop, lights):
    return pop[lights.index(min(lights))]

def get_light_intensities(function, p):
    return [func_file.return_value_function(x, function) for x in p]

def normal(d):
    return np.array([np.random.normal(e, 0.1) for e in range(d)])

def FIREFLY(d, min_, max_, function, g_max, popsize, alpha = 0.3, b_0 = 1):
    result = []
    pop = generate_population(min_, max_, popsize, d)
    lights = get_light_intensities(function, pop)

    for g in range(g_max):
        for i in range(popsize):
            for j in range(popsize):
                if(lights[i] > lights[j]):
                    pop[i] = np.clip(pop[i] + (b_0 / (1 + distance(pop[i], pop[j]))) * (pop[j] - pop[i]) + alpha * normal(d), static_data.get_min_range(function), static_data.get_max_range(function))

                lights[i] = func_file.return_value_function(pop[i], function)
        append_pop = []
        for p in pop:
            pc = list(p.copy())
            print(pc)
            pc.append(func_file.return_value_function(pc, function))
            append_pop.append(pc)
        #best = list(get_best(pop, lights))
        #best.append(func_file.return_value_function(best, function))
        result.append(append_pop)

    return result