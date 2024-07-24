import timeit

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result


def find_min_coins(amount):
    min_coins = [0] + [float("inf")] * amount
    coin_count = [{} for _ in range(amount + 1)]

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] = coin_count[x].get(coin, 0) + 1

    return coin_count[amount]


amounts = [10, 55, 113, 207, 505, 1001]
results = []

for amount in amounts:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=1000)
    results.append([amount, time_greedy, time_dp])

print("Amount | Greedy Time (s) | DP Time (s)")
for result in results:
    print(f"{result[0]:>6} | {result[1]:>14.8f} | {result[2]:>12.8f}")
