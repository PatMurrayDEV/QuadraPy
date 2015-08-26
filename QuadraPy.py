# QuadraPy (c) Patrick Murray 2015
# Command line quadratic equation solver in Python
# My first exploration into Python :/

import math
import os

# Clear the terminal (because neatness is very important)
os.system('cls' if os.name == 'nt' else 'clear')

# Welcome the user (hi user!)
title = "#### QuadraPy ####"
print ('\033[95m' + title.center(80, '#') + '\033[0m')
print "\nThanks for using QuadraPy. QuadraPy is a simple Python based Quadratic equation solver. Pass it the three coefficients and it should spit out one or two real solutions. It does not support imaginary solutions. The source is available at https://github.com/PatMurrayDEV/QuadraPy -- if you have any questions email me at feedback@patmurray.co\n"

# Explain the equation
eq = '\033[42;39m' + "a" + '\033[0m' + " + " + '\033[41;39m' + "b" + '\033[0m' + "x + " + '\033[46;39m' + "c" + '\033[0m' + "x^2"
print "\nFollowing the format " + eq + ",\nEnter the co-efficients (watch for negatives):"


# Get the co-efficients
a = input('\033[42;39m' + "  a" + '\033[0m' + ": ")
b = input('\033[41;39m' + "  b" + '\033[0m' + ": ")
c = input('\033[46;39m' + "  c" + '\033[0m' + ": ")


##### DO THE MATHS!
# To get the discriminate (b^2 - 4ac)
disc = (b**2)-(4*a*c)


# Check the discriminate's value
if disc < 0 :
    print "Sorry, no solution that is _real_ enough for my liking."
elif disc == 0:
    x = (-b + math.sqrt(disc))/(2*a)
    print "One Solution x = ", x
else:
    x1 = (-b + math.sqrt(disc))/(2*a)
    x2 = (-b - math.sqrt(disc))/(2*a)
    print "Two solutions x = ",  x1 ," & ", x2

# END
