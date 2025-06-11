import random as rand

def insertion(A):


    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur

A = ['C', 'B', 'C', 'D', 'A', 'E', 'H', 'G', 'F']
print("List of A before insertion: ", A)
insertion(A)
print("List of A after insertion: ", A)


