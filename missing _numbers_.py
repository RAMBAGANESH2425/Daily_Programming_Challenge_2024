def find_missing_number(arr, n):    
    total_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)
    missing_number = total_sum - actual_sum
    return missing_number
arr = [1, 2, 4, 5, 6]  
n = 6  
print(f"The missing number is: {find_missing_number(arr, n)}")