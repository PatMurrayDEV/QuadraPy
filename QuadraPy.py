# QuadraPy (c) Patrick Murray 2015
# Command line quadratic equation solver in Python
# My first exploration into Python :/

import math

# Welcome the user (hi user!)
print "#### QuadraPy ####"
print "Following the format a + bx + cx^2,\nEnter the co-efficients (watch for negatives):"

# Get the co-efficients
a = input("a: ")
b = input("b: ")
c = input("c: ")

# DO THE MATHS!
# To get the discriminate (b^2 - 4ac)
desc = b**2-4*a*c
print desc

# Check the discriminate's value
if desc < 0 :
    print "Sorry, no solution that is _real_ enough for my liking."
elif desc == 0:
    print "Hell yeah I got me 1 solution"
else:
    print "WOOO two whole solutions!"
