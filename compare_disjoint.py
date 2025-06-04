import random as rand

def disjoint(A, B, C):

    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
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
    print(disjoint(A1, B1, C1))

    n2 = rand.randint(1, 10)
    A2 = [rand.randint(1,20) for i in range(n2)]
    B2 = [rand.randint(1, 20) for i in range(n2)]
    C2 = [rand.randint(1, 20) for i in range(n2)]

    print(A2)
    print(B2)
    print(C2)
    print(disjoint(A2, B2, C2))