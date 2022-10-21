import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from static_data import get_ranges, X
from func_file import return_value_function


def show_2D_graph(routes, points, anim_interval: int = 400):
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
            p = plt.plot([x[final_route[X-1] - 1], x[final_route[0] - 1]], [y[final_route[X-1] - 1], y[final_route[0] - 1]], 'k-')
            lines.append(p)

            return ax
        ani = FuncAnimation(fig, animate, frames=len(routes), interval=anim_interval, repeat=True, fargs=[routes])
    plt.show()
