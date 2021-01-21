message = "lol"
punct = "!"
num = 3

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Using the values of message, punct, and num, print
#a string that looks like the one below if message = "lol",
#punct = "!", and num = 3:
#
# lollollol!lollollol!lollollol
#
#Specifically, it should start by printing message num times,
#then print punct. It should repeat that process num times,
#with punct printed between each time (but not at the start or
#end).
#
#Here are a couple other examples:
#
# message = "bbq", punct = "?", num = 2 -> bbqbbq?bbqbbq
# message = "bbl", punct = ":", num = 3 -> bblbblbbl:bblbblbbl:bblbblbbl
# message = "brb", punct = ".", num = 4 -> brbbrbbrbbrb.brbbrbbrbbrb.brbbrbbrbbrb.brbbrbbrbbrb


#Add your code below!
print((((message*num)+punct)*num),end= -punct)



