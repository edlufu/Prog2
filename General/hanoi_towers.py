def minimum_moves(n):
    if n == 0:
        return 0
    else:
        return 1 + 2 * minimum_moves(n - 1)


x = 50
print(minimum_moves(x))
