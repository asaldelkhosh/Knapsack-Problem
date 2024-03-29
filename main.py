# memory dictionary
memo = {}

"""
solving knapsack problem with recursion.
    n is the total number of items 
    W is the maximum weight the knapsack can carry
"""
def knapsack(W, w, v, n):
    if n == 0 or W == 0:
        return 0

    # if weight of the nth item is more than the weight
    # available in the knapsack the skip it
    if (w[n - 1] > W):
        return knapsack(W, w, v, n - 1)

    # Check if we already have an answer to the subproblem
    if (W, n) in memo:
        return memo[(W, n)]

    # find value of the knapsack when the nth item is picked
    value_picked = v[n - 1] + knapsack(W - w[n - 1], w, v, n - 1)

    # find value of the knapsack when the nth item is not picked
    value_notpicked = knapsack(W, w, v, n - 1)

    # return the maxmimum of both the cases
    # when nth item is picked and not picked
    value_max = max(value_picked, value_notpicked)

    # store the optimal answer of the subproblem
    memo[(W, n)] = value_max

    return value_max


if __name__ == "__main__":
    w = [3, 1, 5, 10, 1, 2, 24, 1]
    v = [10, 5, 7.5, 33, 5, 6, 80, 7.5]
    limit = 30
    n = len(w)

    print(knapsack(limit, w, v, n))
    print(memo)
