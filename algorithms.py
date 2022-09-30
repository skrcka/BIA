import random
import static_data, func_file


def blind_search(name_function: str, size_random_search: int):
    point_list = []
    generated_data_x = [
        random.uniform(static_data.get_min_range(name_function), static_data.get_max_range(name_function))
        for _ in range(size_random_search)]

    generated_data_y = [
        random.uniform(static_data.get_min_range(name_function), static_data.get_max_range(name_function))
        for _ in range(size_random_search)]
    tmp = func_file.return_value_function([generated_data_x[0], generated_data_y[0]], name_function)
    for i, j in zip(generated_data_x, generated_data_y):
        m = func_file.return_value_function([i, j], name_function)
        point_list.append([i, j, m])

    return point_list
    