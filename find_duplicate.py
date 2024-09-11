def find_duplicate(arr):
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = 0
    while (slow != fast):
        slow = arr[slow]
        fast = arr[fast]
    return slow


arr = [1, 4, 4, 2, 3]
print(find_duplicate(arr))
