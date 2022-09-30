import math


ACKLEY_MIN_RANGE = -32.768  #-32.768 -4
ACKLEY_MAX_RANGE = 32.768   #32.768 4
ACKLEY_RANGE = 1 #0.2

LEVY_MIN_RANGE = -10
LEVY_MAX_RANGE = 10
LEVY_RANGE = 0.2

GRIEWANK_MIN_RANGE = -10    #-600
GRIEWANK_MAX_RANGE = 10     #600
GRIEWANK_RANGE = 0.2

RASTRIGIN_MIN_RANGE = -5.12
RASTRIGIN_MAX_RANGE = 5.12
RASTRIGIN_RANGE = 0.1

SCHWEFEL_MIN_RANGE = -500
SCHWEFEL_MAX_RANGE = 500
SCHWEFEL_RANGE = 5

ZAKHAROV_MIN_RANGE = -10
ZAKHAROV_MAX_RANGE = 10
ZAKHAROV_RANGE = 0.2

SPHERE_MIN_RANGE = -5.12
SPHERE_MAX_RANGE = 5.12
SPHERE_RANGE = 0.1

MICHALEWICZ_MIN_RANGE = 0
MICHALEWICZ_MAX_RANGE = math.pi
MICHALEWICZ_RANGE = 0.1

ROSENBROCK_MIN_RANGE = -5
ROSENBROCK_MAX_RANGE = 10
ROSENBROCK_RANGE = 1

ranges = {
    "ackley": (ACKLEY_MIN_RANGE, ACKLEY_RANGE, ACKLEY_MAX_RANGE),
    "levy": (LEVY_MIN_RANGE, LEVY_RANGE, LEVY_MAX_RANGE),
    "griewank": (GRIEWANK_MIN_RANGE, GRIEWANK_RANGE, GRIEWANK_MAX_RANGE),
    "schwefel":  (SCHWEFEL_MIN_RANGE, SCHWEFEL_RANGE, SCHWEFEL_MAX_RANGE),
    "zakharov": (ZAKHAROV_MIN_RANGE, ZAKHAROV_RANGE, ZAKHAROV_MAX_RANGE),
    "sphere": (SPHERE_MIN_RANGE, SPHERE_RANGE, SPHERE_MAX_RANGE),
    "michalewicz": (MICHALEWICZ_MIN_RANGE, MICHALEWICZ_RANGE, MICHALEWICZ_MAX_RANGE),
    "rastrigin": (RASTRIGIN_MIN_RANGE, RASTRIGIN_RANGE, RASTRIGIN_MAX_RANGE),
    "rosenbrock": (ROSENBROCK_MIN_RANGE, ROSENBROCK_RANGE, ROSENBROCK_MAX_RANGE)
}

def get_min_range(name_function):
    if ranges.get(name_function):
        return ranges[name_function][0]
    return 0

def get_max_range(name_function):
    if ranges.get(name_function):
        return ranges[name_function][2]
    return 0

def get_range(name_function):
    if ranges.get(name_function):
        return ranges[name_function][1]
    return 0

def get_ranges(name_function):
    if ranges.get(name_function):
        return ranges[name_function]
    return (0, 0, 0)
