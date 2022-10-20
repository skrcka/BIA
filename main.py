from show_3D_graph import show_funtion_graph
from algorithms.algorithms import get_function
from func_file import func
from algorithms.ga_tsp import get_list_values, generate_list_values
from show_2D_graph import show_2D_graph


def gen_points(algorithm_name: str, function_name: str):
    points = []
    gen_count = 10
    if algorithm_name == 'blind_search':
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
    elif algorithm_name == 'hill_climbing':
        points = get_function('hill_climbing')(function_name, None, None, None, 50, gen_count)
    elif algorithm_name == 'simulated_annealing':
        points = get_function('simulated_annealing')(function_name, None, None, None, 1, 20, gen_count * 10)
    elif algorithm_name == 'differential_evolution':
        points = get_function('differential_evolution')(function_name)

    return points

if __name__ == '__main__':
    algorithm_name = 'ga_tsp_anim' # simulated_annealing ga_tsp
    if algorithm_name not in ('ga_tsp', 'ga_tsp_anim'):
        for function_name in func:
            points = gen_points(algorithm_name, function_name)
            show_funtion_graph(function_name, points)
    elif algorithm_name == 'ga_tsp':
        filename = 'datasets/tps_dataset.txt'
        point_list = get_list_values(filename)
        final_route = get_function(algorithm_name)(point_list)
        show_final_graph(final_route, point_list)
    else:
        filename = 'datasets/tps_dataset.txt'
        #point_list = get_list_values(filename)
        point_list = generate_list_values()
        final_routes = get_function(algorithm_name)(point_list)
        show_2D_graph(final_routes, point_list, anim_interval=50)
    #function_name = 'rosenbrock'
    #points = gen_points(algorithm_name, function_name)
    #show_funtion_graph(function_name, points)
