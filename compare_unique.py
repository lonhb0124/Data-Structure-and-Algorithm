import random as rand
from time import time


""" the worst-case running time of disjoint1 is O(n2) """
def unique1(S):

    for j in range(len(S)):             # O(n) time.
        for k in range(j+1, len(S)):    # O(n) time.
            if S[j] == S[k]:
                print("The duplicate pair in the list is ", S[j])
                return False            # found duplicate pair
    return True
 


""" the worst-case running time of disjoint1 is O(nlog n) """
def unique2(S):

    temp = sorted(S)                    # create a sorted copy of S, O(nlog n) time.
    print("Sorted list is ", temp)
    for j in range(1, len(temp)):             # O(n) time.
        if temp[j-1] == temp[j]:
            print("The duplicate pair in the list is ", temp[j-1])
            return False            # found duplicate pair
    return True

""" the worst-case running time of unique3 is O(2^n) """
def unique3(S, start, stop):        # using Recursion in a wrong way
    if stop - start <= 1 :
        return True
    elif not unique3(S, start, stop - 1):
        return False
    elif not unique3(S, start + 1, stop):
        return False
    else:
        return S[start] != S[stop - 1]
    
if __name__ == '__main__':
    n1 = rand.randint(1, 10)
    A1 = [rand.randint(1,20) for i in range(n1)]

    print(A1)
    print("Test unique1")
    start_time = time()
    print(unique1(A1))
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)

    print("Test unique2")
    start_time = time()
    print(unique2(A1))
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)
