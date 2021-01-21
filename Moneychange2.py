amount = 17

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The variable above describes an amount of money measured in
#dollars. Imagine you want to select the bills (1-dollar bills,
#5-dollar bills, 10-dollar bills, etc.) that make up that
#amount of money. For example, 17 dollars is one $10, one $5,
#and two $1s.
#
#Write a program that will print out the bills needed to
#arrive at the amount shown above. Assume that we always want
#the maximum number of large bills: for example, for 17 dollars,
#we want one $10, one $5, and two $1s, not three $5s and two $1s.
#You may assume that the largest bill you have on hand is a
#$50-dollar bill.
#
#Your code should print the following (with the correct numbers
#based on the value of amount):
#
#Fifties: 0
#Twenties: 0
#Tens: 1
#Fives: 1
#Ones: 2


#Add your code here!
Fifties_val = 50
Twenties_val = 20
Tens_val = 10
Fives_val = 5
Ones_val = 1

Fifties = 0
Twenties = 0
Tens = 0
Fives = 0
Ones = 0

def Fifties_amm():
    return Fifties * Fifties_val
def Twenties_amm():
    return Twenties * Twenties_val
def Tens_amm():
    return Tens * Tens_val
def Fives_amm():
    return Fives * Fives_val
def Ones_amm():
    return Ones * Ones_val

def countdown(): 
    return amount - (Fifties_amm() + Twenties_amm() + Tens_amm() + Fives_amm() + Ones_amm())

Fifties = countdown() // Fifties_val
Twenties = countdown() // Twenties_val
Tens = countdown() // Tens_val
Fives = countdown() // Fives_val
Ones = countdown() // Ones_val

print("Fifties:", Fifties)
print("Twenties:", Twenties)
print("Tens:", Tens)
print("Fives:", Fives)
print("Ones:", Ones)

#print (countdown())