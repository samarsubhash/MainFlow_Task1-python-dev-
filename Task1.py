# Arithmetic Operations
a, b = 5, 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# String Manipulation
str1, str2 = "Hello", "World"
concatenated = str1 + " " + str2
print("Concatenated String:", concatenated)
print("Repeated String:", str1 * 3)
print("Sliced String:", str1[1:4])
print("Uppercase:", str1.upper())
print("Lowercase:", str2.lower())
print("Length of concatenated string:", len(concatenated))

# Conditional Statements
x, y, z = 10, 20, 15
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

if z < x:
    print("z is less than x")
elif x < z < y:
    print("z is between x and y")
else:
    print("z is greater than y")

# Lists
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
fruits.append("orange")
print("List after adding an element:", fruits)
fruits.remove("banana")
print("List after removing an element:", fruits)
for fruit in fruits:
    print(fruit)

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Name:", person["name"])
person["email"] = "alice@example.com"
print("Dictionary after adding an element:", person)
del person["age"]
print("Dictionary after removing an element:", person)
for key, value in person.items():
    print(key, ":", value)

# Tuples
point = (3, 4)
print("X-coordinate:", point[0])
print("Y-coordinate:", point[1])
for coordinate in point:
    print(coordinate)
