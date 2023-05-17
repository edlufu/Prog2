# returnerar antalet combinationer som a kan växlas med coins
def exchange(amount: int, coins: list) -> int:
    if amount == 0:
        return 1
    elif amount < 0 or len(coins) == 0:
        return 0
    else:
        return exchange(amount, coins[1:]) + exchange(amount - coins[0], coins)

# exchange fast returnerar kombinationer av coins
def exchange_combinations(amount: int, coins: list) -> list:
    if amount == 0:
        return []
    elif amount < 0 or len(coins) == 0:
        return []
    

# exchange_combinations fast med begränsade coins
def exch_lim_comb(amount: int, coins: dict) -> list:
    pass

# exchange fast skrivet med memoization
def exchange_memo(amount: int, coins: list) -> int:

    memory = {}

    def ex_memo(a, c):
        key = (a, c)

        value = memory.get(key)
        if value is None:
            if a == 0:
                value = 1
            elif a < 0 or len(c) == 0:
                value = 0
            else:
                value = ex_memo(a, c[1:]) + ex_memo(a - c[0], c)
            memory[key] = value

        return value

    return ex_memo(amount, tuple(coins))


def main():
    a = 12
    coins = [1, 5, 10, 50, 100]

    print(exchange_memo(12, [1, 5, 10, 50, 100]))


if __name__ == '__main__':
    main()
