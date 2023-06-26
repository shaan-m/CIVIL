# Read a space-separated list of numbers from the user
numbers_input = input("Enter a list of numbers (space-separated): ")

# Split the input string into individual numbers
numbers_list = numbers_input.split()

# Convert the numbers from strings to integers
numbers = [int(num) for num in numbers_list]

# Print the array
print(numbers)
