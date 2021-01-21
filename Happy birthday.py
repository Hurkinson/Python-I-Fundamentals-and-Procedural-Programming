current_day = 31
current_month = 5
current_year = 2018
birth_day = 19
birth_month = 12
birth_year = 1990

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Given the current date and birth date held by the variables
#above, calculate and print this person's current age. Note
#that if their birth date has not yet passed this year, your
#result would be one less than if it has.
#
#For example, with the variables given above, the person
#would turn 28 on December 12th, 2018. So, as of May 31st,
#2018, they are 27.


#Add your code here!
years = current_year - birth_year 
#print (years)

def curr_age():
    return  years -1

#print(curr_age())
        
if current_month >= birth_month: 
    years += 1
      
    if current_month == birth_month and current_day < birth_day:
            years -= 1
          
print(curr_age())