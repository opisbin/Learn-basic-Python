names = ["john", "jane", "doe"]
print(names)
# This code initializes a list of names and prints it.

print(names[0])
# This code prints the first element of the names list, which is "john".
print(names[-1])

names[0] = "jon"
print(names[0:2]) 

#list methods

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.remove(3)
print(numbers)

print(len(numbers))
print(numbers.index(4))
