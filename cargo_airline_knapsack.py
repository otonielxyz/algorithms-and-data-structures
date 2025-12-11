"""
cargo_airline_knapsack.py
Author: Otoniel Torres Bernal
Course: CECS 328 – Algorithms (Fall 2025)
Assignment 4 – Cargo Airline Optimization

Description:
    This program solves the classic 0/1 Knapsack Problem using a 1-dimensional
    dynamic programming approach. Given an aircraft's maximum cargo capacity
    and a list of (weight, price) items, the function computes the maximum
    possible revenue the airline can earn while staying within capacity.

    This is equivalent to finding the maximum-value subset of cargo items
    whose total weight does not exceed the aircraft’s limit.

Function:
    aircraft_max_revenue(cargo, capacity)
        - cargo: list of (weight, price) tuples
        - capacity: integer maximum weight allowed
        - returns: maximum revenue (integer)

Algorithm:
    Standard 1D dynamic programming for knapsack:
        dp[w] = maximum revenue achievable with capacity w.
    The DP array is updated backwards to avoid overwriting
    states that are still needed for computation.
"""

def aircraft_max_revenue(cargo, capacity):
    """
    Compute the maximum revenue achievable under weight constraints
    using the 0/1 Knapsack dynamic programming approach.

    Parameters
    ----------
    cargo : list[tuple[int, int]]
        List of (weight, price) tuples for each cargo item.

    capacity : int
        Maximum weight the aircraft can carry.

    Returns
    -------
    int
        Maximum revenue achievable without exceeding capacity.
    """

    # dp[w] = best revenue achievable with capacity w
    dp = [0] * (capacity + 1)

    for weight, price in cargo:
        # Traverse backwards to preserve previous row state
        for w in range(capacity, weight - 1, -1):
            new_val = dp[w - weight] + price
            if new_val > dp[w]:
                dp[w] = new_val

    return dp[capacity]


if __name__ == "__main__":
    # Example:
    # cargo_items = [(10, 60), (20, 100), (30, 120)]
    # cap = 50
    # print(aircraft_max_revenue(cargo_items, cap))  # 220
    pass
