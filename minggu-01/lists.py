squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])

print(squares[:])

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
print(4**3)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)


letters = ['a', 'b', 'c', 'd']
print(len(letters))


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x);

print(x[0])
print(x[0][1])