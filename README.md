# Practicing Genetic Algorithms with the Knapsack Problem
This project serves as an introduction to genetic algorithms in Python. I have built a genetic algorithm using the PyGAD library to solve the 0/1 Knapsack problem with various constraints.

## Constraints
Every item in the problem has a value, weight, and volume. An item's value can range from 1$ to 5$, its weight from 1kg to 7kg, and its volume from 1L to 6L, all with incremental steps of 1 unit. The knapsack can only carry 16kg and has a capacity of 13L.

## Items
The items' data is stored in knapsack_items.csv. There are 50 items in total with randomly generated values, weights, and volumes.

## Simulated Annealing, anyone?
If you're curious to see how simulated annealing compares to a genetic algorithm for this problem, check out my other repository 'knapsack-simulated-annealing'.