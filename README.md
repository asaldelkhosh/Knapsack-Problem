# Knapsack Problem

Sovling knapsack problem with an optimal solution.
The solution to the Knapsack problem uses Recursion with memoization to find the optimal solution.
The algorithm covers all possible cases by considering every item picked and not picked. 
We remember the optimal solution of the subproblem in a hash table, and we reuse the solution instead of recomputing.

## Runtime Complexity

The above solution runs with a complexity of **O(n.W)** where n is the total number of items and W is the maximum weight the knapsack can carry. Although it looks like a polynomial-time solution, it is indeed a pseudo-polynomial time solution.
Given that the computation needs to happen by a factor of W, the maximum times the function will execute will be proportional to the max value of W which will be 2^m where m is the number of bits required to represent the weight W.
This makes the complexity of above solution **O(n.2^m)**. The numeric value of the input W is exponential in the input length, which is why a pseudo-polynomial time algorithm does not necessarily run in polynomial time with respect to the input length.

## Execute

```python
w = [3, 1, 5, 10, 1, 2, 24, 1]
v = [10, 5, 7.5, 33, 5, 6, 80, 7.5]
limit = 30
```

```shell
python main.py
```
