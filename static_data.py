import math


ACKLEY_MIN = -32.768  #-32.768 -4
ACKLEY_MAX = 32.768   #32.768 4
ACKLEY_STEP = 1 #0.2

LEVY_MIN = -10
LEVY_MAX = 10
LEVY_STEP = 0.2

GRIEWANK_MIN = -10    #-600
GRIEWANK_MAX = 10     #600
GRIEWANK_STEP = 0.2

RASTRIGIN_MIN = -5.12
RASTRIGIN_MAX = 5.12
RASTRIGIN_STEP = 0.1

SCHWEFEL_MIN = -500
SCHWEFEL_MAX = 500
SCHWEFEL_STEP = 5

ZAKHAROV_MIN = -10
ZAKHAROV_MAX = 10
ZAKHAROV_STEP = 0.2

SPHERE_MIN = -5.12
SPHERE_MAX = 5.12
SPHERE_STEP = 0.1

MICHALEWICZ_MIN = 0
MICHALEWICZ_MAX = math.pi
MICHALEWICZ_STEP = 0.1

ROSENBROCK_MIN = -5
ROSENBROCK_MAX = 10
ROSENBROCK_STEP = 1

ranges = {
    "ackley": (ACKLEY_MIN, ACKLEY_STEP, ACKLEY_MAX),
    "levy": (LEVY_MIN, LEVY_STEP, LEVY_MAX),
    "griewank": (GRIEWANK_MIN, GRIEWANK_STEP, GRIEWANK_MAX),
    "schwefel":  (SCHWEFEL_MIN, SCHWEFEL_STEP, SCHWEFEL_MAX),
    "zakharov": (ZAKHAROV_MIN, ZAKHAROV_STEP, ZAKHAROV_MAX),
    "sphere": (SPHERE_MIN, SPHERE_STEP, SPHERE_MAX),
    "michalewicz": (MICHALEWICZ_MIN, MICHALEWICZ_STEP, MICHALEWICZ_MAX),
    "rastrigin": (RASTRIGIN_MIN, RASTRIGIN_STEP, RASTRIGIN_MAX),
    "rosenbrock": (ROSENBROCK_MIN, ROSENBROCK_STEP, ROSENBROCK_MAX),
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
