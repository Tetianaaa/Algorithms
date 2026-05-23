import time

def find_coins_greedy(amount, coins):
    result = {}
    coins.sort(key=None, reverse=True)

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result

def find_min_coins(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [None] * (amount + 1)

    for coin in coins:
        for j in range(coin, amount + 1):
            if min_coins[j - coin] + 1 < min_coins[j]:
                min_coins[j] = min_coins[j - coin] + 1
                coin_used[j] = coin

    try:
        result = {}
        current_amount = amount
        while current_amount > 0:
            coin = coin_used[current_amount]
            result[coin] = result.get(coin, 0) + 1
            current_amount -= coin
        return dict(sorted(result.items(), reverse=True))

    except TypeError:
        print(f"It's impossible to give a change for {amount} with coins {coins}")
        return {}

# checking and time testing:
def test_performance():
    coins = [50, 25, 10, 5, 2, 1]
    amounts_to_test = [113, 10143, 50143]

    print("-" * 75)
    print(f"{'Amount':<15} | {'Greedy algorithm time (s)':<22} | {'Dynamic programming time (s)':<22}")
    print("-" * 75)

    for amount in amounts_to_test:
        start_greedy = time.perf_counter()
        for _ in range(1000):
            find_coins_greedy(amount, coins)
        end_greedy = time.perf_counter()
        time_greedy = (end_greedy - start_greedy) / 1000

        start_dp = time.perf_counter()
        for _ in range(10):
            find_min_coins(amount, coins)
        end_dp = time.perf_counter()
        time_dp = (end_dp - start_dp) / 10

        print(f"{amount:<15} | {time_greedy:<25.8f} | {time_dp:<25.8f}")
    print("-" * 75)

if __name__ == "__main__":
    test_performance()