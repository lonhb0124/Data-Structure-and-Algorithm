

""" the running time of linear_sum is O(n) """
# Linear Recursion
def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
    
""" the running time of reverse is O(n) """
# Reversing a Sequence with Recursion - tail recursion
def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)

# Reversing a Sequence with Non Recursion
def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1

""" the running time of power is O(n) """
# Recursive Algorithms for Computing Powers
def power1(x, n):
    if n == 0:
        return 1
    else:
        return x * power1(x, n - 1)

""" the running time of power is O(log n) """  
# Recursive Algorithms for Computing Powers with squaring technique 
def power2(x, n):
    if n == 0:
        return 1
    else: 
        partial = power2(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

""" the running time of binary_sum is O(log n) """ 
def binary_sum(S, start, stop):
    if start >= stop:
        return 0

    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
    
if __name__ == "__main__":

    S1 = [4, 3, 6, 2, 8, 9, 3, 2, 8, 5, 1, 7, 2, 8, 3, 7]
    print(linear_sum(S1, len(S1)))


    S2 = [4, 3, 6, 2, 8]
    print(linear_sum(S2, len(S2)))


    S3 = [4, 3, 6, 2, 8, 9, 5]
    print("The original S3 list: ", S3)
    reverse(S3, 0, len(S3))
    print("After reverse S3 list:", S3)

    x = power1(3, 4)
    print(x)

    x = power2(2, 13)
    print(x)

    S4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_sum(S4, 0,len(S4)))