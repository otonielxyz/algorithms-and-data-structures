"""
rod_cutting_dp.py
Author: Otoniel Torres Bernal
Course: CECS 328 – Algorithms
Programming Assignment 3 – Rod Cutting (Dynamic Programming)

Description:
    This module implements the classic Rod Cutting problem using a bottom-up
    dynamic programming solution. Given a list of prices where price[k-1] is
    the value of a rod piece of length k, the goal is to compute the maximum
    revenue obtainable by cutting a rod of total length n.

    This is equivalent to an unbounded knapsack problem where each piece length
    can be chosen multiple times.

Functions:
    rod_cutting_dp(price, n)
        Computes the maximum obtainable revenue using DP.

    driver_dp(array)
        Measures execution time and prints formatted output for testing.
"""

import time


def rod_cutting_dp(price, n):
    """
    Compute maximum obtainable revenue for a rod of length n using
    bottom-up dynamic programming (unbounded knapsack style).

    Parameters
    ----------
    price : list[int]
        price[k - 1] gives the revenue from a rod piece of length k.

    n : int
        Total rod length.

    Returns
    -------
    int
        Maximum profit achievable.
    """

    # dp[L] = best revenue for rod length L
    dp = [0] * (n + 1)

    # For each target length L, check all piece sizes i <= L
    for L in range(1, n + 1):
        best = 0
        for i in range(1, n + 1):
            if i <= L:
                best = max(best, price[i - 1] + dp[L - i])
        dp[L] = best

    return dp[n]


def driver_dp(array):
    """
    Driver function that accepts a price array and prints:
        - Size of the array
        - Maximum profit
        - Execution time

    Parameters
    ----------
    array : list[int]
        Price list corresponding to rod lengths 1..n.
    """
    n = len(array)
    start = time.time()
    max_profit = rod_cutting_dp(array, n)
    end = time.time()

    print(f"Size of array: {n}")
    print(f"Max profit: {max_profit}")
    print(f"Code execution time: {end - start:.4f} seconds")


if __name__ == "__main__":
    # Example usage (uncomment to run):
    # prices = [1, 5, 8, 9, 10, 17, 17, 20]
    # driver_dp(prices)
    pass
