from tabulate import tabulate

# Example data
data = [
    ["John Doe", 30, "Male"],
    ["Jane Smith", 28, "Female"],
    ["Bob Johnson", 35, "Male"]
]

# Define the table headers
headers = ["Name", "Age", "Gender"]

# Create the table
table = tabulate(data, headers, tablefmt="fancy_grid")

# Print the table
print(table)
