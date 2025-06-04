import random as rand
from time import time


""" the worst-case running time of disjoint1 is O(n3) """
def disjoint1(A, B, C):

    for a in A:                     # O(n) time.
        for b in B:                 # O(n) time.
            for c in C:             # O(n) time.
                if a == b == c:
                    print("The same number between A and B and C is ", a)
                    return False
    return True


""" the worst-case running time of disjoint1 is O(n2) """
def disjoint2(A, B, C):

    for a in A:                 # O(n) time.
        for b in B:             # O(n) time.
            if a == b:          # only check C if a == b
                for c in C:     # depending on the number of same pair between a and b
                    if a == c:
                        print("The same number between A and B and C is ", a)
                        return False
    return True

if __name__ == '__main__':
    n1 = rand.randint(1, 10)
    A1 = [rand.randint(1,20) for i in range(n1)]
    B1 = [rand.randint(1, 20) for i in range(n1)]
    C1 = [rand.randint(1, 20) for i in range(n1)]

    #disjoint(A, B, C)
    print(A1)
    print(B1)
    print(C1)
    start_time = time()
    print(disjoint1(A1, B1, C1))
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)

    start_time = time()
    print(disjoint2(A1, B1, C1))
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)