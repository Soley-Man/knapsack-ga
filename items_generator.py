import os
import csv
import random

# Parameters for item generation
value_range = (1, 5)   # Value in $
weight_range = (1, 7)  # Weight in kg
volume_range = (1, 6)  # Volume in L

# Number of items to generate
num_items = 50

# Generate random items
items = []
for i in range(num_items):
    value = random.randint(*value_range)
    weight = random.randint(*weight_range)
    volume = random.randint(*volume_range)
    
    # Add the item as a tuple
    items.append((f"Item_{i+1}", value, weight, volume))

# Specify the output file
file_name = "knapsack_items.csv"

if os.path.exists(file_name):
    user_input = input("\nCAUTION: Overwrite existing file? y/n ")

if user_input.upper() == "Y":
    # Export the items to a CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["Name", "Value", "Weight", "Volume"])
        # Write item rows
        writer.writerows(items)

    print(f"\nItems successfully exported to {file_name}")

else:
    print("\nOperation canceled")
