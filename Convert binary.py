number = 198

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The number above is given in base 10. Let's convert it to
#base 2 and print it in binary. For example, 215 can be written
#in binary as 11010111.
#
#Each digit of that string corresponds to a power of 2. The far
#left digit represents 128, then 64, then 32, then 16, then 8,
#then 4, then 2, and then finally 1 at the far right.
#
#To convert the number to binary, first check to see if it is
#greater than or equal to 128. If it is, your first digit is 1.
#If not, your first digit is 0. If the number was greater than
#128, subtract 128 (because the 128 is captured by the first
#digit of the string).
#
#Then, repeat that process for 64, 32, 16, 8, 4, 2, and 1.
#
#For example:
#
#215 is >= 128: 1
#87 is >= 64: 11
#23 is not >= 32: 110
#23 is >= 16: 1101
#7 is not >= 8: 11010
#7 is >= 4: 110101
#3 is >= 2: 1101011
#1 is >= 1: 11010111
#
#Note that although we use 'if' a lot to describe this problem,
#this can be done entirely with floor division and modulus.
#Remember, if you convert a boolean to an integer, True becomes
#1 and False becomes 0.
#
#Note that we always work with binary in 8-bit chunks: the
#number 7 would be 00000111, not just 111. That's because inside
#the computer, 8 1s and 0s make a byte, which is the smallest
#practical unit of storage (rarely are bits used outside 8-bit
#bytes).
#
#Print the string that results from this conversion.


#Add your code here!

if number >= 128:
    digit_1 = True
    number -= 128
else: digit_1 = False

if number >= 64:
    digit_2 = True
    number -= 64
else: digit_2 = False

if number >= 32:
    digit_3 = True
    number -= 32
else: digit_3 = False

if number >= 16:
    digit_4 = True
    number -= 16
else: digit_4 = False

if number >= 8:
    digit_5 = True
    number -= 8
else: digit_5 = False

if number >= 4:
    digit_6 = True
    number -= 4
else: digit_6 = False

if number >= 2:
    digit_7 = True
    number -= 2
else: digit_7 = False

if number >= 1:
    digit_8 = True
    number -= 1
else: digit_8 = False

print(int(digit_1),int(digit_2),int(digit_3),int(digit_4),int(digit_5),int(digit_6),int(digit_7),int(digit_8),sep="")