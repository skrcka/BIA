from show_3D_graph import show_funtion_graph
from algorithms import get_function
from func_file import func


def gen_points(algorithm_name: str, function_name: str):
    points = []
    if algorithm_name == 'blind_search':
        gen_count = 10
        point_count = 20
        allpoints = []
        for i in range(gen_count):
            allpoints.append(get_function(algorithm_name)(function_name, point_count))
        total_min_point = None
        for i in range(len(allpoints)):
            generation = allpoints[i]
            min_point = min(generation, key=lambda point: point[2])
            if not total_min_point or min_point[2] < total_min_point[2]:
                total_min_point = min_point
            points.append(total_min_point)
    return points

if __name__ == '__main__':
    algorithm_name = 'blind_search'
    for function_name in func:
        points = gen_points(algorithm_name, function_name)
        show_funtion_graph(function_name, points)
