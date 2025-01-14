import pygad
import random
import csv

# Knapsack constraints
max_weight = 16  # in kg
max_volume = 13  # in L

# File containing the items
items_file = "knapsack_items.csv"

# Define the fitness function
def fitness_func(ga_instance, solution, solution_idx):
    value = 0
    weight = 0
    volume = 0

    # Evaluate each item in the knapsack
    for idx, gene in enumerate(solution):
        if gene == 1:
            item = items[idx]
            value += item["Value"]
            weight += item["Weight"]
            volume += item["Volume"]
    
    # Return the value of all items if they respect the constraints, else penalize fitness
    if weight > max_weight or volume > max_volume:
        return -(weight + volume)
    else:
        return value

# Read the csv file containing the items
with open(items_file, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    items = [{"Name" : row[0],
              "Value" : int(row[1]),
              "Weight" : int(row[2]),
              "Volume" : int(row[3])} for row in reader]

# Genetic algorithm parameters
num_generations = 100
num_parents_mating = 4

sol_per_pop = 10
initial_population = [random.choices([0, 1], k=len(items)) for _ in range(sol_per_pop)]

parent_selection_type = "tournament"

fitness_function = fitness_func
crossover_type = "two_points"

mutation_probability = 0.05
mutation_by_replacement = True
random_mutation_min_val = 0
random_mutation_max_val = 1
gene_space = [0, 1]

stop_criteria = None  # replace with e.g. "reach_30" to stop once fitness ≥ 30

# Define and run the genetic algorithm
ga_instance = pygad.GA(num_generations = num_generations,
                       num_parents_mating = num_parents_mating,
                       sol_per_pop = sol_per_pop,
                       initial_population = initial_population,
                       parent_selection_type = parent_selection_type,
                       fitness_func = fitness_function,
                       crossover_type = crossover_type,
                       mutation_probability = mutation_probability,
                       mutation_by_replacement = mutation_by_replacement,
                       random_mutation_min_val = random_mutation_min_val,
                       random_mutation_max_val = random_mutation_max_val,
                       gene_space = gene_space,
                       stop_criteria = stop_criteria)

ga_instance.run()

# Print results
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(f"Parameters of the best solution : {solution}")
print(f"Fitness value of the best solution = {solution_fitness}")
