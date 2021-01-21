num = 3

#-----------------------------------------------------------
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write some code that calculates the cube of the number
#given by num. Then, print that number num^2 (num squared)
#times in a row, with no spaces or line breaks in between.
#
#For example, if num is 3, then your code would print:
#
# 272727272727272727
#
#That 27 9 times. 3 squared is 9, 3 cubed is 27, and so
#it prints 27 9 times.
#
#Note: these directions are slightly different from the
#preview we posted! You should be printing num^3 num^2
#times, not printing num^2 num^3 times.


#Add your code here!

x = num*num*num
y = num*num

print("{0}".format(x)*y)

