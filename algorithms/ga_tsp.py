import numpy as np
import math
import random
import matplotlib.pyplot as plt


FILENAME = "datasets/tps_dataset.txt"

def get_list_values(filename):
    with open(filename, 'r') as f:
        all_lines = [[int(num) for num in line.split()] for line in f]
    return all_lines


def distance(node1, node2):
    return math.sqrt(((node1[1] - node2[1]) ** 2) + ((node1[2] - node2[2]) ** 2))


def create_matrix(list_nodes):
    matrix = np.zeros((len(list_nodes), len(list_nodes)))
    for j in range(len(list_nodes)):
        for i in range(len(list_nodes)):
            if j != i:
                matrix[i, j] = distance(list_nodes[i], list_nodes[j])
                matrix[j, i] = distance(list_nodes[i], list_nodes[j])

    matrix.tolist()
    return matrix


def generated_population():
    return random.sample(range(1, 21), 20)


def generated_list_population(num_population):
    list = []
    for i in range(num_population):
        list.append(generated_population())
    return list


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
    for i in [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19]:
        result_list.append(list_A[i])
    for i in range(len(list_A)):
        if list_B[i] not in result_list:
            result_list.insert(7, list_B[i])
    result_list = mutation(result_list)
    return result_list


def cal_total_dist(list_points, matrix):
    sum = 0
    for i in range(18):
        sum += matrix[list_points[i] - 1][list_points[i + 1] - 1]
    return sum


def cross_population(list_population, num_first_population, matrix):
    result_list = []
    for i in range(num_first_population):
        while True:
            j = random.randint(0, num_first_population - 1)
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


def final_population(num_first_population, num_generations, matrix):
    list_population = generated_list_population(num_first_population)
    for i in range(num_generations):
        print(i)
        list_population = cross_population(list_population, num_first_population, matrix)
    return list_population


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


def show_final_graph(final_route, filename):
    list_nodes = get_list_values(filename)
    x = []
    y = []
    for i in list_nodes:
        x.append(i[1])
        y.append(i[2])
    plt.plot(x, y, "go")
    for i in range(len(final_route) - 1):
        plt.plot([x[final_route[i] - 1], x[final_route[i + 1] - 1]], [y[final_route[i] - 1], y[final_route[i + 1] - 1]],
                 'k-')
    plt.plot([x[final_route[19] - 1], x[final_route[0] - 1]], [y[final_route[19] - 1], y[final_route[0] - 1]], 'k-')
    plt.show()
