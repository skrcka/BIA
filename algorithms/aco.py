import math
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

FILENAME = "datasets/tps_dataset.txt"

ITERATIONS = 200
NUM_ANTS = 50
EVAPORATION = 0.5
ALPHA = 1
BETA = 2
POINT_COUNT = 21


def generate_list_values():
    point_list = []
    for i in range(1, POINT_COUNT):
        point_list.append([i, random.randint(0, 300), random.randint(0, 300)])
    return point_list


def get_list_values(filename):
    with open(filename, 'r') as f:
        all_lines = [[int(num) for num in line.split()] for line in f]
    return all_lines


def distance(node1, node2):
    return math.sqrt(((node1[1] - node2[1]) ** 2) + ((node1[2] - node2[2]) ** 2))


def first_matrix_visibility(matrix):
    visibility = 1 / matrix
    visibility[visibility == np.inf] = 0
    return visibility


def create_matrix(list_nodes):
    matrix = np.zeros((len(list_nodes), len(list_nodes)))
    for j in range(len(list_nodes)):
        for i in range(len(list_nodes)):
            if j != i:
                matrix[i, j] = distance(list_nodes[i], list_nodes[j])
                matrix[j, i] = distance(list_nodes[i], list_nodes[j])

    matrix.tolist()
    return matrix


def cal_total_dist(list_points, matrix):
    sum = 0
    for i in range(POINT_COUNT - 2):
        sum += matrix[int(list_points[i]) - 1][int(list_points[i + 1]) - 1]
    return sum


def ACO(matrix, num_ants, iter, alpha, beta, evap):
    matrix = matrix
    num_cities = len(matrix[0])
    visibility = first_matrix_visibility(matrix)
    pheromne = np.ones((num_ants, num_cities))
    route = np.ones((num_ants, num_cities + 1))
    all_routes = []
    for _ in range(iter):
        route[:, 0] = 1
        for i in range(num_ants):
            temp_visibility = np.array(visibility)
            for j in range(num_cities - 1):
                cur_loc = int(route[i, j] - 1)
                temp_visibility[:, cur_loc] = 0
                p_feature = np.power(pheromne[cur_loc, :], beta)
                v_feature = np.power(temp_visibility[cur_loc, :], alpha)
                p_feature = p_feature[:, np.newaxis]
                v_feature = v_feature[:, np.newaxis]

                combine_feature = np.multiply(p_feature, v_feature)
                total = np.sum(combine_feature)
                prob = np.cumsum(combine_feature / total)

                r = random.uniform(0, 1)
                city = np.argmax(prob > r) + 1
                route[i, j + 1] = city

        dist_route = np.zeros((num_ants, 1))
        for i in range(num_ants):
            dist_route[i] = cal_total_dist(route[i], matrix)
        dist_min_loc = np.argmin(dist_route)
        best_route = route[dist_min_loc, :]
        pheromne = (1 - evap) * pheromne
        for l in range(num_ants):
            for m in range(num_cities-1):
                d = 1/dist_route[l]
                pheromne[int(route[l,m]) - 1, int(route[l, m + 1]) - 1] = pheromne[int(route[l, m]) - 1, int(route[l, m + 1]) - 1] + d
        all_routes.append([int(x) for x in best_route])
    best_route = [int(x) for x in best_route]
    return all_routes, best_route


def show_final_graph(final_route, list_nodes):
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

def show_final_graph_2(routes, points, anim_interval: int = 400):
    x = []
    y = []
    for i in points:
        x.append(i[1])
        y.append(i[2])
    fig = plt.figure()
    ax = plt.plot(x, y, "go")
    lines = []
    if routes:
        def animate(i, routes):
            print(f'frame: {i}')
            nonlocal lines
            for line in lines:
                for l in line:
                    l.remove()
            lines = []

            final_route = routes[i]
            for i in range(len(final_route) - 1):
                p = plt.plot([x[final_route[i] - 1], x[final_route[i + 1] - 1]], [y[final_route[i] - 1], y[final_route[i + 1] - 1]],
                        'k-')
                lines.append(p)
            p = plt.plot([x[final_route[POINT_COUNT-1] - 1], x[final_route[0] - 1]], [y[final_route[POINT_COUNT-1] - 1], y[final_route[0] - 1]], 'k-')
            lines.append(p)

            return ax
        ani = FuncAnimation(fig, animate, frames=len(routes), interval=anim_interval, repeat=True, fargs=[routes])
    plt.show()


def main():
    #matrix = create_matrix(get_list_values(FILENAME))
    list_values = generate_list_values()
    matrix = create_matrix(list_values)
    #best_route = ACO(FILENAME, NUM_ANTS, ITERATIONS, ALPHA, BETA, EVAPORATION)
    routes, best_route = ACO(matrix, NUM_ANTS, ITERATIONS, ALPHA, BETA, EVAPORATION)
    #print(f'Best route: {best_route}')
    #dist = cal_total_dist(best_route, matrix)
    dist = cal_total_dist(routes[-1], matrix)
    print(f'Distance route: {dist}')
    show_final_graph(best_route, list_values)
    show_final_graph_2(routes, list_values,50)


if __name__ == "__main__":
    main()
