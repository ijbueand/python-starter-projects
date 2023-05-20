# Type Conversion
birth_year = int(input('Enter your birth year: '))
age = 2022 - birth_year
print ('You are ' + str(age) + ' years old')
print ('You are', age, 'years old')

# Strings
course = 'Python for Beginners'
#         0123456789...
print(course)
print(course.upper())
print(course.lower())
print(course.find('for'))
print(course.replace('for', '4'))
print('Python' in course)

# Arithmetic Operators
print(10+3)
print(10-3)
print(10/3) # División Float
print(10//3) # División Int
print(10%3) # Resto de la división
print(10*3) # Multiplicación normal
print(10**3) # Potencia

# Augmented Assignment Operators
x = 10
x + 1 y lo almacena en x
x = x + 1 # Da 11 y lo almacena en x
x += 1 # Da 11 y lo almacena en x
x -= 1 # Da 9 y lo almacena en x
x *= 1 # Da 10 y lo almacena en x

# Comparison Operators: >, >=, <, <=, ==, !=
x = 3 > 2 
print(x) # Devuelve True
x = 3 == 2 
print(x) # Devuelve False
x = 3 != 2 
print(x) # Devuelve True

# Logical Operators: and(both), or(either), not(invert)
price = 25
price > 10 and price < 30 # Devuelve True porque las dos son True
price > 10 or price < 30 # Devuelve True porque las dos son True
price = 5
price > 10 and price < 30 # Devuelve False porque la primera es False aunque la segunda sea True
price > 10 or price < 30 # Devuelve True porque la segunda es True
not price > 10 # Devuelve True porque hemos negado el False resultante de la operación

# If statements: if, elif, else 
t = 25

if t > 30:
    print("It's a hot day") # Look at the use of  " instead of '
    print('Drink plenty of water')
elif t > 20:
    print("It's a nice day") # The if iteration ends here, since this is true
elif t > 10:
    print("It's a bit cold") # Even if this is also true, the iteration has ended
                             # This is because we have used else if 
else:
    print("It's cold!!")
print('Done!')

# Exercise with If statements
w = float(input('Weigh:'))
u = (input('(K)g OR (L)bs:')).upper()
if u == 'K':
    w *= 2.20462
    print('Weigh in Lbs:', w)
elif u == 'L':
    w /= 2.20462
    print('Weigh in Kg:', w)
else:
    print('Error')  

# While loops
i = 1
while i <= 1_000: # The _ is to make it more readable, but it doesn't matter
    print(i)
    i += 1
    
# Lists
names = ["John", "Bob", "Mosh", "Sam"]
#         0       1      2       3
print(names[2]) # Pulls up 'Mosh'
print(names[-1]) # Pulls up 'Sam'
print(names[-2]) # Pulls up 'Mosh'
names[2] = 'Yennesi'
print(names[2]) # Pulls up 'Yennesi'
print(names[0:3]) # Pulls up from 0 to 2 (the last one does not pulls up)
print(names[0:4]) # Pulls up from 0 to 3 (the last one pulls up)
print(names[-2]) # Pulls up 'Yennesi'

# List methods
numbers = [1,2,3,4,5]
numbers.append(6) # Añade al final de la lista
print(numbers)
numbers.insert(0, -1) # Añade -1 al comienzo de la lista
print(numbers)
numbers.remove(3) # Quita el 3 de la lista
print(numbers)
numbers.clear() # Borra la lista
print(numbers)
numbers = [1,2,3,4,5]
print(1 in numbers) # Devuelve True si 1 está en la lista
print(len(numbers)) # Devuelve la longitud de la lista
print(numbers)

# For loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found 
# in other object-orientated programming languages.
n = [2,3,4,5,6,7,8]
for i in n:
    print(i) # Devuelve la lista, uno por uno

# Ranges
numbers = range(5) # Cero to four
for number in numbers:
    print(number)
numbers = range(5,10) # Five to nine
for number in numbers:
    print(number)
for number in range(101):
    print(number) # Pulls up from 0 to 100
    
# Tuples 
numbers = (1, 2, 3, 3)
numbers[0] = 3 # Error. Tuples are immutable.
numbers.count(3) # Result: 2
