"""
rod_cutting_recursive.py
Author: Otoniel Torres Bernal
Course: CECS 328 – Algorithms
Programming Assignment 3 – Rod Cutting (Recursive Solution)

Description:
    This module implements the classical rod cutting problem using a pure
    recursive (top-down, no memoization) approach. Given a list of prices
    where price[k-1] corresponds to the value of a rod piece of length k,
    the algorithm computes the maximum revenue obtainable by cutting a rod
    of length n into smaller pieces.

    This implementation is intentionally exponential in time complexity
    (O(2^n)) because it explores all possible ways of cutting the rod
    without memoization. It serves as a contrast to the bottom-up dynamic
    programming version.

Functions:
    rod_cutting_recursive(price, i, n)
        Computes the maximum obtainable revenue with recursion.

    driver_recursive(array)
        Executes the algorithm, measures runtime, and prints formatted output.
"""

import time


def rod_cutting_recursive(price, i, n):
    """
    Pure recursive solution to the rod cutting problem.

    Parameters
    ----------
    price : list[int]
        price[k - 1] gives the value of a rod piece of length k.

    i : int
        The current piece length being considered (from n down to 1).

    n : int
        Remaining rod length.

    Returns
    -------
    int
        Maximum revenue achievable using piece lengths up to i
        to construct a rod of length n.

    Notes
    -----
    - This is an exponential-time algorithm (O(2^n)).
    - For each piece length i, we consider:
        1) NOT taking the piece and decreasing i
        2) Taking the piece (if possible) and staying at i (unbounded use)
    """

    # Base cases: no rod left or no piece sizes left
    if i == 0 or n == 0:
        return 0

    # Option 1: Do NOT take piece of length i → move to smaller piece size
    not_take = rod_cutting_recursive(price, i - 1, n)

    # Option 2: Take the piece (if it fits) and stay at i (unbounded)
    take = float('-inf')
    if i <= n:
        take = price[i - 1] + rod_cutting_recursive(price, i, n - i)

    return max(take, not_take)


def driver_recursive(array):
    """
    Driver for the recursive rod cutting algorithm.

    Parameters
    ----------
    array : list[int]
        Price array of size n, where array[k - 1] is the value of piece length k.

    Prints
    ------
    - Size of the array
    - Max profit computed
    - Execution time (seconds)
    """
    n = len(array)
    start = time.time()
    max_profit = rod_cutting_recursive(array, n, n)
    end = time.time()

    print(f"Size of the array: {n}")
    print(f"Max profit: {max_profit}")
    print(f"Code execution time: {end - start:.4f} seconds")


if __name__ == "__main__":
    # Example usage:
    # prices = [1, 5, 8, 9, 10, 17, 17, 20]
    # driver_recursive(prices)
    pass
