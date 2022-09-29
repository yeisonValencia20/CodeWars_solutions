# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# MI CODIGO
import math
def zero(operation = None):
    if(operation):
        return math.floor(eval('0' + operation))
    return '0' 
def one(operation = None):
    if(operation):
        return math.floor(eval('1' + operation))
    return '1' 
def two(operation = None):
    if(operation):
        return math.floor(eval('2' + operation))
    return '2' 
def three(operation = None):
    if(operation):
        return math.floor(eval('3' + operation))
    return '3' 
def four(operation = None):
    if(operation):
        return math.floor(eval('4' + operation))
    return '4' 
def five(operation = None):
    if(operation):
        return math.floor(eval('5' + operation))
    return '5' 
def six(operation = None):
    if(operation):
        return math.floor(eval('6' + operation))
    return '6' 
def seven(operation = None):
    if(operation):
        return math.floor(eval('7' + operation))
    return '7' 
def eight(operation = None):
    if(operation):
        return math.floor(eval('8' + operation))
    return '8' 
def nine(operation = None):
    if(operation):
        return math.floor(eval('9' + operation))
    return '9' 

def plus(number):
    return ' + ' + number 
def minus(number):
    return ' - ' + number 
def times(number):
    return ' * ' + number 
def divided_by(number):
    return ' / ' + number 

print(seven(times(five())))
print(four(plus(nine())))


# CODIGO CON MEJORES PRACTICAS
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y

