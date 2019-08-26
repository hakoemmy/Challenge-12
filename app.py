def solve(n, coins, k):
    """
    Solution for count_change

    :param n: money
    :param coins: List of coins.
    :param k: coins[k]
    :return: Count of combinations.
    """

    # print("n: %d, k: %d" % (n, k))
    if k < 0 or n < 0:
        return 0

    if n == 0:  # Change for 0 is only empty one.
        return 1

    # print("  n: %d, k: %d" % (n, k - 1))
    # print("  n: %d, k: %d" % (n - coins[k], k))
