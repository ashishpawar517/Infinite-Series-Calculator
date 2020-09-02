
# for math functionalities
import math as m
# for high precision float handling
from decimal import *
# for argument parsing command line
import argparse
# for docstrings and text dedent
import textwrap
# import time
# color codes
CRED = '\033[91m'
CGREEN= '\033[92m'
CYELLOW='\033[33m'
CEND = '\033[0m'
# Basic Math function definitions
def log(n):
    return m.log10(n)

def ln(n):
    return m.log(n)

def fact(n):
    return m.factorial(n)

def sin(n):
    return m.sin(n)

def cos(n):
    return m.cos(n)

def tan(n):
    return m.tan(n)

def sqrt(n):
    return m.sqrt(n)

def cuberoot(n):
    return n**(1/3)

# command line argument processing
parser = argparse.ArgumentParser(
    prog='series_calc', formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
         Current supported Math functions in Infinite series!
         ---------------------------------------------------
            1. log(n) = log of n to the base 10
            2. ln(n) = log of n to the base e
            3. fact(n) = factorial of n or n!
            4. sin(n) = trigonometric sin(x)
            5. cos(n) = trigonometric cos(x)
            6. tan(n) = trigonometric tan(x)
            7. sqrt(n) = square root of a number
            8. cuberoot(n) = cuberoot of a number
         '''))
parser.add_argument('-u ', '--upper', type=int,
                    default=500, help='max # no of terms')
parser.add_argument('-l ', '--lower', type=int, default=1,
                    help='min term to start with infinite series ')
parser.add_argument(
    '-f', nargs='*', help='function for infinite series (function should be in terms of n)', required=True)
parser.add_argument('-s', type=int, default=32, help='set new precision')
parser.add_argument('-v', '--version', action='version',
                    version='series_calc.py - 1.0')
args = parser.parse_args()

# first argument
# print(args.f[0])
try:
# create a lambda function using eval
    fn = eval('lambda n:' + args.f[0])
# fn = eval(fn)

# set new precision 
    getcontext().prec = args.s

# infinite series
# as this is going to be a finite series but as the principle hypothesis in infinite series states that
# any convergent infinite series will converge to some arbitrary constant after some iteration.
    res = Decimal(0.0)

    upper_limit = args.upper
    lower_limit = args.lower
    for i in range(lower_limit, upper_limit+1):
        res = res + Decimal(fn(i))
        if i%6 == 1:
            print(CYELLOW,"[._____] : =>", res,CEND,end='\r')
        elif i%6 == 2:
            print(CYELLOW,"[__.___] : =>", res,CEND,end='\r')
        elif i%6 == 3:
            print(CYELLOW,"[___.__] : =>", res,CEND,end='\r')
        elif i%6 == 4:
            print(CYELLOW,"[____._] : =>", res,CEND,end='\r')
        elif i%6 == 5:
            print(CYELLOW,"[_____.] : =>", res,CEND,end='\r')
        else:
            print(CYELLOW,"[______] : =>", res,CEND,end='\r')
        
        # time.sleep(1.0)
    
    # printing the result
    print(CGREEN,"[OUTPUT] : =>", res,CEND,end="\r")

except ZeroDivisionError as identifier:
    print(CRED,'[ERROR] Please change the lower limit. (start with 1)',CEND)

except SyntaxError as identifier:
    print(CRED,'[ERROR] Please check the function provided. (missing brackets or incomplete/incompatible operation)',CEND)

except OverflowError as identifier:
    print(CRED,'[ERROR] Please check the function provided. (Max limit Reached) last value found =',res,CEND)
