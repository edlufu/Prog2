# räknar potenser rekursivt
def pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return (1 / x) * pow(x, n + 1)
    else:
        return x * pow(x, n - 1)


# pow med mwe effektiv algoritm
def powerpow(x, n):
    def sqr(x):
        return x * x

    if n < 0:
        return (1 / x) * powerpow(x, n + 1)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return sqr(powerpow(x, n / 2))
    else:
        return x * sqr(powerpow(x, (n - 1) / 2))


print(powerpow(2, 10000))
