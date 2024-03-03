# List of numbers
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# Check if any number is greater than 3
result = any(num > 3 for num in numbers)
# Print the result
print(result)  # Output: True
