import math


ACKLEY_MIN = -32.768  #-32.768 -4
ACKLEY_MAX = 32.768   #32.768 4
ACKLEY_STEP = 1 #0.2
ACKLEY_SIGMA = 5 #0.2

LEVY_MIN = -10
LEVY_MAX = 10
LEVY_STEP = 0.2
LEVY_SIGMA = 1

GRIEWANK_MIN = -10    #-600
GRIEWANK_MAX = 10     #600
GRIEWANK_STEP = 0.2
GRIEWANK_SIGMA = 1

RASTRIGIN_MIN = -5.12
RASTRIGIN_MAX = 5.12
RASTRIGIN_STEP = 0.1
RASTRIGIN_SIGMA = 0.5

SCHWEFEL_MIN = -500
SCHWEFEL_MAX = 500
SCHWEFEL_STEP = 5
SCHWEFEL_SIGMA = 20

ZAKHAROV_MIN = -10
ZAKHAROV_MAX = 10
ZAKHAROV_STEP = 0.2
ZAKHAROV_SIGMA = 1

SPHERE_MIN = -5.12
SPHERE_MAX = 5.12
SPHERE_STEP = 0.1
SPHERE_SIGMA = 0.5

MICHALEWICZ_MIN = 0
MICHALEWICZ_MAX = math.pi
MICHALEWICZ_STEP = 0.1
MICHALEWICZ_SIGMA = 0.5

ROSENBROCK_MIN = -5
ROSENBROCK_MAX = 10
ROSENBROCK_STEP = 0.1
ROSENBROCK_SIGMA = 0.1

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

sigmas = {
    "ackley": ACKLEY_SIGMA,
    "levy": LEVY_SIGMA,
    "griewank": GRIEWANK_SIGMA,
    "schwefel": SCHWEFEL_SIGMA,
    "zakharov": ZAKHAROV_SIGMA,
    "sphere": SPHERE_SIGMA,
    "michalewicz": MICHALEWICZ_SIGMA,
    "rastrigin": RASTRIGIN_SIGMA,
    "rosenbrock": ROSENBROCK_SIGMA,
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

def get_sigma(name_function):
    if sigmas.get(name_function):
        return sigmas[name_function]
    return 0
