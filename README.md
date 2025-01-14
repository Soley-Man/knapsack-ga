# knapsack-ga
This project serves as an introduction to genetic algorithms in Python. I will use a genetic algorithm to solve the 1/0 Knapsack problem with various constraints.

Every item has a value, weight, and volume.
An item's value can range from 1$ to 5$, its weight from 1kg to 7kg, and its volume from 1L to 6L (all with incremental steps of 1 unit).
The knapsack can only carry 16kg and has a capacity of 13L.

items_generator.py creates items at random and exports them in a csv file, which is then read by knapsack_ga.py. The reason for storing items in an external file is to allow comparing different algorithms to solve the same problem (e.g. simulated annealing vs genetic algorithm).