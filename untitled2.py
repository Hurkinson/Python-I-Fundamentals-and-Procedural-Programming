'''
current_hour = 12
current_minute = 37
current_section = "PM"
due_hour = 9
due_minute = 0
due_section = "AM"
'''
'''
current_hour = 2
current_minute = 24
current_section = "AM"
due_hour = 2
due_minute = 45
due_section = "AM"
'''

current_hour = 12
current_minute = 37
current_section = "AM"
due_hour = 9
due_minute = 0
due_section = "AM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Given the current time and deadline time represented by the
#variables above, determine if an assignment is still eligible
#for submission. An assignment is eligible if the time
#represented by current_hour, current_minute, and
#current_section is before the time represented by due_hour,
#due_minute, and due_section.


#Add your code here!
import datetime
def a():
    return current_hour
def b():
    return current_minute
def c():
    return current_section
def x():
    return due_hour
def y():
    return due_minute
def z():
    return due_section
    
'''if (c() == "AM" and z() == "AM"):
    if a() < x():'''
        
current_time = [a(),b(),c()]
due_time = [x(),y(),z()]

#print(current_time)
#print(due_time)

result = current_time <= due_time

print(a() <= x())
print(b() <= y())
print(c() <= z())
print(result)
