
#!/usr/bin/env python3

def greet_programmer():
   print("Hello, programmer!")

def greet(name = "Naureen"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Sunny")


def add(num1, num2):
    return num1 + num2
    num1 = 1
    num2 = 2
    sum = add(num1, num2)

def halve(number):
   return number / 2
   number = 4