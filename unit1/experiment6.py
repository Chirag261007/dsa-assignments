def binary(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary(arr, key, low, mid - 1)
    else:
        return binary(arr, key, mid + 1, high)


arr = list(map(int, input("Enter sorted elements: ").split()))
k = int(input("Enter element to search: "))

res = binary(arr, k, 0, len(arr) - 1)

if res == -1:
    print("Not found")
else:
    print("Found at index", res)