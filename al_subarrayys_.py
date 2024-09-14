def find_subarrays_with_zero_sum(arr):
    # Dictionary to store the sum and their corresponding indices
    sum_dict = {}
    sum_dict[0] = [-1]  # Initialize sum 0 at index -1
    current_sum = 0
    result = []
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        # If current_sum exists in the dictionary, it means there's a subarray with zero sum
        if current_sum in sum_dict:
            for start_index in sum_dict[current_sum]:
                result.append((start_index + 1, i))
                
        # Append the current index to the list of indices where this sum occurs
        if current_sum not in sum_dict:
            sum_dict[current_sum] = []
        sum_dict[current_sum].append(i)
    
    return result

# Example usage:
arr = [1, 2, -3, 3, -1, 2]
result = find_subarrays_with_zero_sum(arr)
print(result)  # Output: [(0, 2), (1, 3)]
