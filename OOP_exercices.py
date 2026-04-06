# OPERATOR OVERLOADING

"""
Problem 1
"""

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - self.imag)

    def __repr__(self):
        return f"{self.real} + {self.imag}j"
    

"""
Problem 2
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def compare(self, other):
        return self.age > other.age

p1 = Person("John", 30, "Male")
p2 = Person("Jane", 25, "Female")

# print(p1.compare(p2))

#correction
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __gt__(self, other):
        return self.age > other.age
    
p1 = Person("John", 30, "Male")
p2 = Person("Jane", 25, "Female")

# print(p1 > p2) # True


"""
Problem 4
"""

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

v1 = Vector(1, 2, 3)
v2 = Vector(3, 2, 1)
# print(v1.dot(v2))

#correction
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

v1 = Vector(1, 2, 3)
v2 = Vector(3, 2, 1)
# print(v1 * v2)


"""
Problem 5
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def __lt__(self, other):
        return self.radius < other.radius
        
    def __le__(self, other):
        return self.radius <= other.radius
        
    def __eq__(self, other):
        return self.radius == other.radius
        
    def __ne__(self, other):
        return self.radius != other.radius
        
    def __gt__(self, other):
        return self.radius > other.radius
        
    def __ge__(self, other):
        return self.radius >= other.radius
        
c1 = Circle(5)
c2 = Circle(6)
# print(c1 < c2) # Output: True
# print(c1 > c2) # Output: False
# print(c1 == c2) # Output: False


"""
Problem 6
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()

p1 = Point(1, 1)
p2 = Point(2, 2)

# print(p1 < p2) # True
# print(p1 == p2) # False


"""
Problem 7
"""
    
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Incompatible dimensions")
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                sum = 0
                for k in range(len(other.matrix)):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)
        
    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.matrix)
        
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = m1 * m2
# print(m3)


# INHERITANCE
"""
Problem 1
"""
class Vehicle:
    def drive(self):
        return "Driving a vehicle"

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"
    
"""
Problem 2
"""
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old and I live at {self.address}."

class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        Person.__init__(self, name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"My name is {self.name}, I am studying {self.field_of_study}."

class Employee(Person):
    def __init__(self, name, age, address, company):
        Person.__init__(self, name, age, address)
        self.company = company
    
    def introduce(self):
        return f"My name is {self.name}, I work at {self.company}."
    

p = Person("Alice", 30, "Paris")
s = Student("Bob", 22, "Lyon", "Computer Science")
e = Employee("Charlie", 40, "London", "Google")

print(p.introduce())
print(s.introduce())
print(e.introduce())


"""
Problem 3
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            False
    def transfer(self, destination_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.deposit(amount)
            return True
        else:
            return False
        
class SavingAccounts:
    def __init__(self, account_number, balance, interest_rate):
        BankAccount.__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
    
    def check_balance(self):
        return self.check_balance
    
