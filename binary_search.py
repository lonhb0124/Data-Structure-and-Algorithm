
""" the running time of binary_search is O(log n) for sorted sequence """
# - tail recursion
def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = (low + high) // 2     # floor division O(log n) time
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

# - non recursive
def binary_search_iterative(data, target):

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

        
if __name__ == "__main__":

    A = [2, 4, 5, 6, 7, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    
    print(binary_search(A, 22, 0, len(A)-1))