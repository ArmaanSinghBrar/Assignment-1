#Converting seconds into minutes and seconds
Seconds = int(input("Enter number of seconds="))
a = Seconds//60   #a is the number of minutes
b = Seconds%60    #b is the number of seconds
print(a,"Minutes and",b,"Seconds")
