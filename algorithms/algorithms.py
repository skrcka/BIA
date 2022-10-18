import random
import numpy as np
import math

from static_data import get_max_range, get_min_range, get_sigma
from func_file import return_value_function
from algorithms.ga_tsp import *


def blind_search(name_function: str, size_random_search: int):
    point_list = []
    generated_data_x = [
        random.uniform(get_min_range(name_function), get_max_range(name_function))
        for _ in range(size_random_search)]

    generated_data_y = [
        random.uniform(get_min_range(name_function), get_max_range(name_function))
        for _ in range(size_random_search)]
    tmp = return_value_function([generated_data_x[0], generated_data_y[0]], name_function)
    for i, j in zip(generated_data_x, generated_data_y):
        m = return_value_function([i, j], name_function)
        point_list.append([i, j, m])

    return point_list

def hill_climbing(name_function, mux, muy, sigma, size, iterat):
    point_list = []
    if not mux:
        mux = random.uniform(get_min_range(name_function), get_max_range(name_function))
    if not muy:
        muy = random.uniform(get_min_range(name_function), get_max_range(name_function))
    if not sigma:
        sigma = get_sigma(name_function)
    generated_x = np.clip(np.random.normal(mux, sigma, size), get_min_range(name_function), get_max_range(name_function))
    generated_y = np.clip(np.random.normal(muy, sigma, size), get_min_range(name_function), get_max_range(name_function))
    tmp = return_value_function([mux, muy], name_function)
    cord_X = generated_x[0]
    cord_Y = generated_y[0]
    for i, j in zip(generated_x, generated_y):
        k = return_value_function([i, j], name_function)
        if k < tmp:
            tmp = k
            cord_X = i
            cord_Y = j
    point_list.append([cord_X, cord_Y, tmp])
    if iterat == 1:
        return point_list
    else:
        return point_list + hill_climbing(name_function, cord_X, cord_Y, sigma, size, iterat - 1)

def simulated_annealing(name_function, mux, muy, sigma, size, temperature, iterat):
    temperature_decrease = lambda temperature: temperature * 0.95
    temperature_min = 0.01
    point_list = []
    if not mux:
        mux = random.uniform(get_min_range(name_function), get_max_range(name_function))
    if not muy:
        muy = random.uniform(get_min_range(name_function), get_max_range(name_function))
    if not sigma:
        sigma = get_sigma(name_function)
    generated_x = np.clip(np.random.normal(mux, sigma, size), get_min_range(name_function), get_max_range(name_function))
    generated_y = np.clip(np.random.normal(muy, sigma, size), get_min_range(name_function), get_max_range(name_function))
    tmp = return_value_function([mux, muy], name_function)
    cord_X = generated_x[0]
    cord_Y = generated_y[0]

    while temperature > temperature_min:
        generated_x = np.clip(np.random.normal(mux, sigma, size), get_min_range(name_function), get_max_range(name_function))
        generated_y = np.clip(np.random.normal(muy, sigma, size), get_min_range(name_function), get_max_range(name_function))
        for i, j in zip(generated_x, generated_y):
            m = return_value_function([i, j], name_function)
            if m < tmp:
                tmp = m
                cord_X = i
                cord_Y = j
            else:
                r = random.uniform(0, 1)
                if r < math.exp(-(m - tmp) / temperature):
                    tmp = m
                    cord_X = i
                    cord_Y = j
            point_list.append([cord_X, cord_Y, tmp])
            if len(point_list) >= iterat:
                return point_list
        temperature = temperature_decrease(temperature)
    return point_list

def ga_tsp_anim(point_list):
    print(point_list)
    distance_matrix = create_distance_matrix(point_list)
    final_list = get_population_anim(40, 10000, distance_matrix)
    final_routes = []
    for pop in final_list:
        final_routes.append(get_best_route_in_population(pop, distance_matrix))
    return final_routes

def ga_tsp(point_list):
    print(point_list)
    distance_matrix = create_distance_matrix(point_list)
    final_list = final_population(40, 10000, distance_matrix)
    routes = get_best_route_in_population(final_list, distance_matrix)
    return routes

functions = {
    'blind_search': blind_search,
    'hill_climbing': hill_climbing,
    'simulated_annealing': simulated_annealing,
    'ga_tsp': ga_tsp,
    'ga_tsp_anim': ga_tsp_anim,
}

def get_function(function_name: str):
    return functions.get(function_name)
