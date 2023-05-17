"""  MA4_1.2

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Joacim Stenlund
Date reviewed: 16/05
"""

import random
import math
import functools


def hypersphere(N: int, d: int, r=1.0) -> float:
    """
    Estimates volyme of "d"-dimensional hypersphere with the radius "r"
    using Monte Carolo method with "N" number of samples, returns estimated value
    """
    # creates "N" random samples within range with coordinates for all "d" dimensions
    samples = [[random.uniform(-r, r) for _ in range(d)] for _ in range(N)]

    # filters samples inside hypersphere,
    # if sum of the coordnaties to the power of 2 smaller than radius squared
    samples_sphere = list(
        filter(
            lambda coord: functools.reduce(
                lambda x, y: x + y, map(lambda x: x**2, coord)
            )
            <= r**2,
            samples,
        )
    )
    # counts number of samples in hypersphere
    N_sphere = len(samples_sphere)

    # calulates estimated hypersphere volume
    V = lambda r, d: (2 * r) ** d
    V_hs = (N_sphere / N) * V(r, d)
    return V_hs


def hypersphere2(N: int, d: int, r=1.0) -> float:
    "Hypersphere w/o a bunch of higher order functions cramed into it"
    samples = [[random.uniform(-r, r) for _ in range(d)] for _ in range(N)]
    N_sphere = len(
        list(filter(lambda coord: sum(map(lambda x: x**2, coord)) <= r**2, samples))
    )
    V = (2 * r) ** d
    return (N_sphere / N) * V


def hypersphere_exact(d, r=1):
    return ((math.pi ** (d / 2)) / math.gamma(d / 2 + 1)) * r**d


if __name__ == "__main__":
    n = 100000
    d = 2
    print(hypersphere(n, d))
    print(hypersphere_exact(d))
