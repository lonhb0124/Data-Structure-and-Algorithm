import sys
import ctypes
from time import time

class DynamicArray:

    def __init__(self):

        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
        
    def __getitem__(self, k):

        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):

        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        
        return (c * ctypes.py_object)()
    
    def insert(self, k, value):
        # we assume 0 <= k <= n
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):

        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self.A[j] = self._A[j + 1]
                self._n -= 1
            return
        raise ValueError('value not found')


# Test DynamicArray Class 
""" 
A = DynamicArray()
print(A.__len__())
A.append(3)
print(A.__len__())
print(A.__getitem__(0))
A.append(20)
print(A.__getitem__(1))
"""

# extending a list
data = []
n = 27
for k in range(n):
    a = len(data)                   # number of elements
    b = sys.getsizeof(data)         # actual size in bytes
    # print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)               # increase length by one
print(data)
# constructing new list
square = []
for k in range(1, n + 1):
    square.append(k * k)
print(square)

square2 = [k*k for k in range(1, n + 1)]
print(square2)

"""

Length 0 : 56 bytes
Length 1 ~ 4  : Length 0 + 32 bytes
Length 5 ~ 8  : Length 0 ~ 4 + 32 bytes
Length 9 ~ 16 : Length 0 ~ 8 + 64 bytes
Length 17 ~ 24 : Length 0 ~ 16 + 64 bytes
Length 25 ~ 26 : Length 0 ~ 24 + 64 bytes

""" 

def compute_average(n):

    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) * 1000000 / n      # change to ns from s

def compute_insert_average(n, case):

    data = []
    start = time()
    if case == "beginning":
        for k in range(n):
            data.insert(0, None)

    elif case == "middle":
        for k in range(n):
            data.insert(k // 2, None)

    elif case == "end":
        for k in range(n):
            data.insert(k, None)

    end = time()
    return (end - start) * 1000000 / n      # change to ns from s




n = [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
"""
for i in n:
    print('Compute average time is {0:2.3f}us; n is {1:6d}'.format(compute_average(i), i))

"""
# insert at the beginning of a list is most expensive
# beginning > middle > end
N = [100, 1000, 10000, 100000, 1000000]

"""
for j in N:
    print('Compute insert average time at the beginning of a list is {0:2.3f}us; N is {1:6d}'.format(compute_insert_average(j, "beginning"), j))

#insert near the middle of a list
for j in N:
    print('Compute average time near the middle of a list is {0:2.3f}us; N is {1:6d}'.format(compute_insert_average(j // 2, "middle"), j))

# insert at the end of the list
for j in N:
    print('Compute average time at the end of the list is {0:2.3f}us; N is {1:6d}'.format(compute_insert_average(j, "end"), j))
"""


