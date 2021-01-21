can_afford = True
destination_is_safe = True
educational_value = False
relatives_nearby = False
is_international = True
have_passport = True
afraid_to_fly = False
have_a_car = True
is_a_beach = True
is_warm = True
has_skiing = False
is_a_city = False
is_off_peak = False
has_attraction = False

if can_afford and destination_is_safe:
    result1 = True       
    
elif not can_afford and destination_is_safe and (educational_value or relatives_nearby):
    result1 = True
    
else: result1 = False

print("result1 =",result1)


if is_international: 
    if have_passport:
        if not afraid_to_fly:
            result2 = True
            
        else: result2 = False    
    else: result2 = False      
else:
    
    if have_a_car or not afraid_to_fly:
        result2 = True
    else: result2 = False
    
print("result2 =", result2)
 
if is_a_beach and is_warm:
     Beach_ok = True
else: 
    Beach_ok = False
    
if not is_warm and has_skiing:
        Ski_ok = True
        Beach_ok = False
else:
    Ski_ok = False  
                          
     
if is_a_city and (is_off_peak or has_attraction):
    City_ok = True
            
else: City_ok = False
 

result3 = Beach_ok or Ski_ok or City_ok

print("result3 =", result3)


print(result1 and result2 and result3)


