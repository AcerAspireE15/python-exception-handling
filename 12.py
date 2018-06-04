def function1(a, b):
    print(a+b)
    print(a*b)
    print(a-b)
    print(a/b)
    print(a%b)
function1(20, 3)
print('hello')

try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('there is a divide by zero error')

try:
    a = 20
    b = 10
    print(a/b)
except ZeroDivisionError:
    print('there is a divide by zero error')

try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('there is a divide by zero error')
finally:
    print('this is going to execute no matter what')

try:
    a = 20
    b = 10
    print(a/b)
except ZeroDivisionError:
    print('there is a divide by zero error')
finally:
    print('this is going to execute no matter what')