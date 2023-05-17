def fakultet(n):
    result = 1
    if n > 0:
        result = n * fakultet(n - 1)
    return result
