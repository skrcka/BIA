import numpy as np
import math
import random
import matplotlib.pyplot as plt
import random
from static_data import X


FILENAME = "datasets/tps_dataset.txt"

def generate_list_values():
    point_list = []
    for i in range(1, X+1):
        point_list.append([i, random.randint(0, 300), random.randint(0, 300)])
    return point_list

def get_list_values(filename):
    with open(filename, 'r') as f:
        point_list = [[int(num) for num in line.split()] for line in f]
    return point_list


def distance(node1, node2):
    return math.sqrt(((node1[1] - node2[1]) ** 2) + ((node1[2] - node2[2]) ** 2))


def create_distance_matrix(list_nodes):
    distance_matrix = np.zeros((len(list_nodes), len(list_nodes)))
    for j in range(len(list_nodes)):
        for i in range(len(list_nodes)):
            if j != i:
                distance_matrix[i, j] = distance(list_nodes[i], list_nodes[j])
                distance_matrix[j, i] = distance(list_nodes[i], list_nodes[j])

    distance_matrix.tolist()
    return distance_matrix


def generate_population():
    return random.sample(range(1, X+1), X)


def generate_list_population(num_population):
    l = []
    for i in range(num_population):
        l.append(generate_population())
    return l


def mutation(x):
    r = random.uniform(0, 1)
    if r < 0.5:
        while True:
            m = random.randint(1, len(x) - 1)
            n = random.randint(1, len(x) - 1)
            if m != n:
                break
        tmp = x[n]
        x[n] = x[m]
        x[m] = tmp
    return x


def cross_population_gen(list_A, list_B):
    result_list = []
    cross_point = random.randint(1, X-1)
    result_list = list_A[:cross_point]
    for i in range(len(list_A)):
        if list_B[i] not in result_list:
            result_list.append(list_B[i])
    result_list = mutation(result_list)
    return result_list


def cal_total_dist(list_points, matrix):
    sum = 0
    for i in range(X-2):
        sum += matrix[list_points[i] - 1][list_points[i + 1] - 1]
    return sum


def cross_population(list_population, population_size, matrix):
    result_list = []
    for i in range(population_size):
        while True:
            j = random.randint(0, population_size - 1)
            if i != j:
                break
        dist_parent_A = cal_total_dist(list_population[i], matrix)
        x = cross_population_gen(list_population[i], list_population[j])
        dist = cal_total_dist(x, matrix)
        if dist_parent_A > dist:
            result_list.append(x)
        else:
            result_list.append(list_population[i])
    return result_list


def final_population(population_size, gen_count, matrix):
    list_population = generate_list_population(population_size)
    for i in range(gen_count):
        print(i)
        list_population = cross_population(list_population, population_size, matrix)
    return list_population

def get_population_anim(population_size, gen_count, matrix):
    list_population = generate_list_population(population_size)
    populations = [list_population]
    for i in range(gen_count):
        print(i)
        list_population = cross_population(list_population, population_size, matrix)
        populations.append(list_population)
    return populations


def get_best_route_in_population(list_population, matrix):
    min = 90000
    best_route = []
    for i in list_population:
        dist = cal_total_dist(i, matrix)
        if min > dist:
            min = dist
            best_route = i
    print("")
    print("Min:" + str(min))
    print(best_route)
    return best_route


def show_final_graph(final_route, points):
    x = []
    y = []
    for i in points:
        x.append(i[1])
        y.append(i[2])
    plt.plot(x, y, "go")
    for i in range(len(final_route) - 1):
        plt.plot([x[final_route[i] - 1], x[final_route[i + 1] - 1]], [y[final_route[i] - 1], y[final_route[i + 1] - 1]],
                 'k-')
    plt.plot([x[final_route[X-1] - 1], x[final_route[0] - 1]], [y[final_route[X-1] - 1], y[final_route[0] - 1]], 'k-')
    plt.show()
