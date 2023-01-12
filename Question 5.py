#Sine and Cosine values between 0 and 345 with 15 increments
import math
for i in range(0,346,15):
    Sine = math.sin(math.radians(i))
    Cosine = math.cos(math.radians(i))
    print(i,"---",round(Sine,4),round(Cosine,4))
