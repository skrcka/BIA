import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from static_data import get_ranges
from func_file import return_value_function


def show_funtion_graph(name_function: str, points: list or None = None, anim_interval: int = 400):
    start, step, stop = get_ranges(name_function)
    range_list = np.arange(start, stop, step)
    
    X = [i for i in range_list for _ in range_list]
    Y = list(range_list) * len(range_list)

    Z = [return_value_function([x, y], name_function) for x, y in zip(X, Y)]

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_trisurf(X, Y, Z, alpha=0.6, edgecolor='none')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    active_point = None

    if points:
        def animate(i, points):
            print(f'frame: {i}')
            nonlocal active_point
            if active_point:
                if type(active_point) is list:
                    for ap in active_point:
                        ap.remove()
                else:
                    active_point.remove()

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            
            point = points[i]
            if type(point[0]) is list:
                active_point = []
                for p in point:
                    active_point.append(ax.scatter(p[0], p[1], p[2], c='red'))
            else:
                active_point = ax.scatter(point[0], point[1], point[2], c='red')

            return ax
        ani = FuncAnimation(fig, animate, frames=len(points), interval=anim_interval, repeat=True, fargs=[points])
    plt.show()
