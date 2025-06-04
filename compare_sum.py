from time import time
import random as rand


""" the running time of sum is O(n) """
def sum(S):
    
    n = len(S)                      # constant time
    total = 0
    for j in range(n):              
        total += S[j]               # O(n) time.
    return total

""" the running time of even_index_sum is O(n) """
def even_index_sum(S):
    
    n = len(S)                      # constant time
    total = 0
    for j in range(0, n, 2):        # increment of 2        
        total += S[j]               # O(n) time.
    return total

""" the running time of prefix sum1 is O(n^2) """
def prefix_sum1(S):
    
    n = len(S)                      # constant time
    total = 0
    for j in range(n):
        for k in range(1+j):            # O(n) time.
            total += S[k]               # O(n) time.
    return total

""" the running time of prefix sum2 is O(n) """
def prefix_sum2(S):
    
    n = len(S)                      # constant time
    total = 0
    prefix = 0
    for j in range(n):    
        prefix += S[j]        
        total += prefix               # O(n) time.
    return total

""" the running time of prefix sum3 is O(n^3) """
def prefix_sum3(S, B):
    
    n = len(S)                      # constant time
    count = 0
    for j in range(n):              
        total = 0
        for i in range(n):          
            for k in range(1+j):    # O(n) time.
                total += A[k]       # O(n) time.
        if B[i] == total:
            count += 1               # O(n) time.
    return count

def measure_function_time(func, *args):
    start_time = time()
    result = func(*args)
    end_time = time()
    elapsed = end_time - start_time
    print(f"[{func.__name__}] Result is: {result}")
    print(f"[{func.__name__}] Running time is: {elapsed}")
    print()

if __name__ == "__main__":
    n = rand.randint(1, 10)
    A = [rand.randint(1, 20) for i in range(n)]
    B = [rand.randint(1, 20) for i in range(n)]
    print("The list A is ", A)
    print("The list B is ", B)

    measure_function_time(sum, A)
    measure_function_time(even_index_sum, A)
    measure_function_time(prefix_sum1, A)
    measure_function_time(prefix_sum2, A)
    measure_function_time(prefix_sum3, A, B)