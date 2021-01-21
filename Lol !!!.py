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
# !!!lollollol!!!lollollol!!!lollollol!!!
#
#Specifically, it should start by printing punct num
#times, then print message num times, repeat that entire
#process num times, and then print punct num times
#again.
#
#Here are a couple other examples:
#
# message = "bbl", punct = ":", num = 1 -> :bbl:
# message = "bbq", punct = "?", num = 2 -> "??bbqbbq??bbqbbq??
# message = "brb", punct = ".", num = 4 -> ....brbbrbbrbbrb....brbbrbbrbbrb....brbbrbbrbbrb....brbbrbbrbbrb....


#Add your code below!
print((((punct*num)+(message*num))*num)+(punct*num))