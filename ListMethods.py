numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(0,10)
numbers.remove(5)
numbers.pop()
print(numbers.index(2))
print(10 in numbers)
print(numbers.count(4))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(10)
numbers.append(100)
numbers.append(21)
print(numbers)

# tuples are immutable
numbers = (1, 2, 3)
numbers.count(numbers)

coordinates = (1, 2, 3)
coordinates = [1, 2, 3]
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates
print(x)
print(y)
print(z)
print(coordinates)
