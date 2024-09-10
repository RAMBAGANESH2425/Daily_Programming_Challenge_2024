def find_missing_number(arr, n):
    # Calculate the expected sum of first n natural numbers
    total_sum = n * (n + 1) // 2
    # Calculate the sum of elements in the array
    actual_sum = sum(arr)
    # The missing number is the difference between expected and actual sum
    missing_number = total_sum - actual_sum
    return missing_number

# Example usage
arr = [1, 2, 4, 5, 6]  # Example array, missing number is 3
n = 6  # The total number of elements including the missing one
print(f"The missing number is: {find_missing_number(arr, n)}")
