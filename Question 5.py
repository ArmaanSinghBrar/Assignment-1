#Sine and Cosine values between 0 and 345 with 15 increments
import math
for i in range(0,346,15):                          #running a loop till 345 with 15 increments
    Sine = math.sin(math.radians(i))
    Cosine = math.cos(math.radians(i))
    print(i,"---",round(Sine,4),round(Cosine,4))        #Rounding value for Sine and Cosine till 4 decimal places
