import csv
import random

# Number of rows and columns
n = 35
m = 25

# Open a new CSV file
with open('random_matrix.csv', 'w', newline='') as csvfile:
  # Create a CSV writer
  writer = csv.writer(csvfile)

  # Create a list of rows
  rows = [[random.randint(8, 9) for j in range(m)] for i in range(n)]
  print(rows)

  # Write the rows to the CSV file
  writer.writerows(rows)

print('Done')
