from time import time

def prefix_average1(S):
    n = len(S)                      # constant time
    A = [0] * n                     # O(n) time.
    for j in range(n):
        total = 0                   # O(n) time.
        for i in range(j + 1):
            total += S[i]           # O(n^2) time 
        A[j] = total / (j + 1)      # O(n) time.

    return A

def prefix_average2(S):

    n = len(S)                      # constant time
    A = [0] * n                     # O(n) time.
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j + 1)      # O(n) time.

    return A

if __name__ == "__main__":

    x = [35, 1, 20, 100, 120, 40, 30, 10, 20, 50]
    start_time = time()
    print(prefix_average1(x))
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)

    start_time = time()
    print(prefix_average2(x))
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)

