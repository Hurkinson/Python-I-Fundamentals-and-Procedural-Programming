busy = True
hungry = False
tired = True
stressed = False

Happy = busy and not stressed
Sad = hungry or tired
Confused = Happy and Sad      
Bored = not Happy and not Sad and not busy
Anxious = not Happy and not Sad and stressed

"""Happy = busy and not stressed
print("Happy:",Happy)
Sad = hungry or tired
print("Sad:",Sad)
Confused = Happy and Sad   
print("Confused:",Confused)   
Bored = not Happy and not Sad and not busy
print("Bored:",Bored)
Anxious = not Happy and not Sad and stressed
print("Anxious:",Anxious)"""

print ("Happy: ", Happy, '\n', "Sad: ", Sad,'\n', "Confused: ", Confused,
       '\n', "Bored: ", Bored, '\n', "Anxious: ", Anxious, sep="")