
""" the running time of bad_fibonacci is O(2^n) """
def bad_fibonacci(n):
    
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)

""" the running time of good_fibonacci is O(n) """
def good_fibonacci(n):

    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

print(bad_fibonacci(6))
print(bad_fibonacci(6))