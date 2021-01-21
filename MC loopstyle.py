amount = 50

quarters_value = 25
dimes_value = 10
nickels_value = 5
pennies_value = 1
quarters = 0
dimes = 0
nickels = 0
pennies = 0

quarters_amm = quarters * quarters_value
dimes_amm = dimes_value * dimes
nickels_amm = nickels_value * nickels
pennies_amm = pennies_value * pennies

def countdown(): 
    return amount - (quarters_amm + dimes_amm + nickels_amm + pennies_amm)

while quarters_amm <= countdown() :
    quarters += 1
    quarters_amm = quarters * quarters_value

while dimes_amm < countdown() :
    dimes += 1
    dimes_amm = dimes * dimes_value

while nickels_amm < countdown() :
    nickels += 1
    nickels_amm = nickels * nickels_value
    
while pennies_amm < countdown() :
    pennies += 1
    pennies_amm = pennies * pennies_value


print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
