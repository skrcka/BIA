from show_3D_graph import show_funtion_graph
from algorithms import blind_search
from func_file import func


if __name__ == '__main__':
    point_count = 20
    gen_count = 10
    for fn in func:
        points = []
        for i in range(gen_count):
            points.append(blind_search(fn, point_count))
        show_funtion_graph(fn, points)
