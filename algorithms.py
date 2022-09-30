import random
import numpy as np

from static_data import get_max_range, get_min_range
from func_file import return_value_function


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
    generated_x = np.random.normal(mux, sigma, size)
    generated_y = np.random.normal(muy, sigma, size)
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
    
functions = {
    'blind_search': blind_search,
    'hill_climbing': hill_climbing,
}

def get_function(function_name: str):
    return functions.get(function_name)
