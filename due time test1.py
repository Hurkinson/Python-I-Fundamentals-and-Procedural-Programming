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

curr_day = datetime.date(2020, 10, 27)
due_day = datetime.date(2020, 10, 27)


def current():
    return curr_day, datetime.time(current_hour, current_minute, 0), current_section
def due():
    return due_day, datetime.time(due_hour, due_minute, 0), due_section

if current_section == "PM":
    current_hour += 12
    if current_hour == 24:
        current_hour = 0
        current_section = "AM"
        curr_day += datetime.timedelta(days=1)
        
if due_section == "PM":
    due_hour += 12
    if due_hour == 24:
        due_hour = 0
        due_section = "AM"
        due_day += datetime.timedelta(days=1)
        
#if current_hour >= 12:
    #current_section = "PM"

#if due_hour >= 12:
    #due_section = "PM"

print("current:",current())
print("due:",due())
a = current() < due()

print(a)

