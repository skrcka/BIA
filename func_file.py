import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def ackley(input_data):
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum1 = np.array(input_data)
    sum1 = np.sum(sum1 ** 2)

    sum2 = np.array(input_data)
    sum2 = np.cos(c * sum2)
    sum2 = np.sum(sum2)

    term1 = - a * np.exp(-b * math.sqrt((1 / len(input_data)) * sum1 ** 2))
    term2 = - np.exp((1 / len(input_data)) * sum2)

    return term1 + term2 + a + np.exp(1)


def levy(input_data):
    sum1 = 0
    for i in range(len(input_data)):
        w = 1 + ((input_data[i] - 1) / 4)
        wd = 1 + ((input_data[len(input_data) - 1] - 1) / 4)
        sum1 = sum1 + ((((w - 1) ** 2) * (1 + (10 * math.sin(math.pi * w + 1))**2)) + (((wd - 1) ** 2) * (
                1 + math.sin(2 * math.pi * wd) ** 2)))
    return (math.sin(math.pi * (1 + (input_data[0] - 1) / 4)) ** 2) + sum1


def griewank(input_data):
    sum1 = [(item ** 2) / 4000 for item in input_data]
    sum2 = 1
    for i, item in enumerate(input_data):
        sum2 = sum2 * math.cos(item / ((i + 1) ** .5))
    return sum(sum1) - sum2 + 1


def rastrigin(input_data):
    sum = 0
    for item in input_data:
        sum = sum + (item ** 2 + - 10 * math.cos(2 * np.pi * item))
    return 10 * len(input_data) + sum


def schwefel(input_data):
    sum1 = 0
    for item in input_data:
        sum1 = sum1 + item * math.sin((abs(item)) ** .5)
    return 418.9829 * len(input_data) - sum1


def zakharov(input_data):
    sum1 = sum([item**2 for item in input_data])
    sum2 = sum([(0.5 * i * item) for i, item in enumerate(input_data, start=1)])
    result = sum1 + sum2**2 + sum2**4
    return result


def sphere(input_data):
    sum1 = np.array(input_data)
    return np.sum(sum1 ** 2)


def michalewicz(input_data):
    m = 10
    sum1 = 0
    for i, item in enumerate(input_data):
        sum1 = sum1 + ((math.sin(item)) * (((math.sin((i + 1) * item ** 2)) / math.pi) ** (2 * m)))
    return -(sum1)

def rosenbrock(input_data):
    sum = 0
    for i, p in enumerate(input_data):
        sum += 100 * (input_data[i] - p ** 2) ** 2 + (p - 1) ** 2
    return sum

func = {
    "ackley": ackley,
    "levy": levy,
    "griewank": griewank,
    "schwefel":  schwefel,
    "zakharov": zakharov,
    "sphere": sphere,
    "michalewicz": michalewicz,
    "rastrigin": rastrigin,
    "rosenbrock": rosenbrock,
}

def return_value_function(input_data,name_function):
    if func.get(name_function):
        return func[name_function](input_data)
    return 0
