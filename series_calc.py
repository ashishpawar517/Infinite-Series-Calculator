
# for argument parsing command line
import argparse
# for docstrings and text dedent
import textwrap
# import mpmath lib
from mpmath import * 
import sys
# color codes
CRED = '\033[91m'
CGREEN= '\033[92m'
CYELLOW='\033[33m'
CEND = '\033[0m'

# command line argument processing
parser = argparse.ArgumentParser(
    prog='series_calc', formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
         Current supported Math functions in Infinite series!
         ---------------------------------------------------
            1. log(n) = log of n to the base 10
            2. ln(n) = log of n to the base e
            3. fac(n) = factorial of n or n!
            4. sin(n) = trigonometric sin(x)
            5. cos(n) = trigonometric cos(x)
            6. tan(n) = trigonometric tan(x)
            7. sqrt(n) = square root of a number
            8. cbrt(n) = cuberoot of a number
         '''))
parser.add_argument('-u ', '--upper',
                    default='inf', help='max # no of terms')
parser.add_argument('-l ', '--lower', type=int, default=1,
                    help='min term to start with infinite series')
parser.add_argument(
    '-f', nargs='*', help='function for infinite series (function should be in terms of n)', required=True)
parser.add_argument('-p', type=int, default=50, help='set new precision')
parser.add_argument('-v', '--version', action='version',
                    version='series_calc.py - 1.0')
args = parser.parse_args()

try:
    mp.dps =args.p
    lower_limit = args.lower
    upper_limit = args.upper
    fn = None 
    str_cmd = "nsum(lambda n:"+args.f[0]+",["+str(lower_limit)+","+str(upper_limit)+"])"
    # print(str_cmd)
    fn = eval(str_cmd)        
    res = fn
    print(CGREEN,"[OUTPUT] : =>", res,CEND,end="\r")

except ZeroDivisionError as e :
    print(CRED,'[ERROR] Check the lower limit provided (Please change it to 1) ',CEND)
# 
except SyntaxError :
    print(CRED,'[ERROR] Please check the function provided. (missing brackets or incomplete/incompatible operation)',CEND)

except  NameError:
    print(CRED,'[ERROR] Please check the function provided. (incompatible function .see help)',CEND)
