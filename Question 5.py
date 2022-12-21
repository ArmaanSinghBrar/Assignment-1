#Sine and Cosine values between 0 and 345 with 15 increments
import math
pie = 3.14
i = 0
for i in range(0,346,15) :
     a = math.sin(math.radians(i))    #a is the values of sine function
     b = math.cos(math.radians(i))    #b is the values of cosine function
     print( i , " --- " , round(a,4),round(b,4))
