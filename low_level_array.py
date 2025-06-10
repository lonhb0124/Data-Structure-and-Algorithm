from array import array

""" REferential Arrays """

primes = [2, 3, 5, 7, 11, 13, 17, 19]

# elements of the list are immutable objects
temp = primes[3:6]
print("List of primes: ", primes," List of temp: ",  temp)
temp[2] = 15
print("List of primes: ", primes," List of temp: ",  temp)



# elements of the list are immutable objects
backup = list(primes)
print("List of primes: ", primes," List of backup: ",  backup)
backup[2] = 15
print("List of primes: ", primes," List of backup: ",  backup)



# all eight cells of the list reference the same object
data = [0] * 8
print("List of data: ", data)
data[2] += 1
print("List of data: ", data)

# extend list receives references to those elements
extras = [23, 29, 31]
print("List of primes: ", primes)
primes.extend(extras)
print("List of primes: ", primes)



""" Compact Arrays """
# using array library module to reduce elecment of bit from 64-bits to 16-bits
primes2 = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
print("List of primes: ", primes2)
print(primes2[0])

