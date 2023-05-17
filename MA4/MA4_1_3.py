"""  MA4_1.3

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Joacim Stenlund
Date reviewed: 16/05
"""

import concurrent.futures as future
import time
from MA4_1_2 import hypersphere


def hypersphere_time(n: int, d: int):
    """Times hypersphere function with "n" samples and "d" dimensions"""

    start = time.perf_counter()

    result = hypersphere(n, d)

    end = time.perf_counter()

    return result, round(end - start, 4)


def multip_hypersphere_time(n: int, d: int, p: int):
    """Times hypersphere function with "n" samples and "d" dimensions, using "p" number of processes"""

    if n % p != 0:
        raise ValueError("Samples(n) need to be devisable by number of processes(p)")

    else:
        npp = int(n / p)
        samp = [npp for _ in range(p)]
        dim = [d for _ in range(p)]

        start = time.perf_counter()

        with future.ProcessPoolExecutor() as ex:
            results = ex.map(hypersphere, samp, dim)
        mean_result = sum(results) / p
        end = time.perf_counter()

        return mean_result, round(end - start, 4)


if __name__ == "__main__":
    n = 10000000
    d = 11
    p = 10

    r1, t1 = hypersphere_time(n, d)
    r2, t2 = multip_hypersphere_time(n, d, p)

    print(
        f"""
Single process with {n} samples in {d} dimensions took: {t1} s
Yielded estimeted volyme of: {r1} volume units

{p} parallel processes dividing the total {n} samples, in {d} dimensions, took: {t2} s
Yielded estimeted volyme of: {r2} volume units
"""
    )


# ----------- results of program ---------------------------------------------------------------------------
"""Single process with 10000000 samples in 11 dimensions took: 91.529 s
Yielded estimeted volyme of: 1.8806784 volume units

10 parallel processes dividing the total 10000000 samples, in 11 dimensions, took: 27.6708 s
Yielded estimeted volyme of: 1.8757632000000002 volume units"""
