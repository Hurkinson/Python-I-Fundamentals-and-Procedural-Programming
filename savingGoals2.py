principal = 40000
rate = 0.05
years = 5
goal = 50000

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Last problem, we calculated how much money a person would
#have to invest to reach a certain savings goal. Now, let's
#modify that to instead take a principal, interest rate,
#number of years, and savings goal, and report whether or not
#the person will meet their savings goal.
#
#Add some code below that will calculate whether the
#investment described by the values above will meet the given
#goal. If it will, print True. If it will not, print False.
#
#As a reminder, the formula for the value of an account after
#a given time (in number of years) is:
#
#  Current Value = principal * e ^ (rate * number of years)
#
#Remember, you can access e using math.e as long as you don't
#change the next line. You don't need to worry about rounding
#on this problem.
import math


#Add your code here!
a = principal * math.e**(rate*years)

invest = (round(a,2))

result = invest >= goal

print(result)

