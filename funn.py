def has_duplicates(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False

# Example usage:
my_array = [1, 2, 3, 4, 5, 2]
if has_duplicates(my_array):
    print("Array has duplicate elements.")
else:
    print("Array does not have duplicate elements.")
