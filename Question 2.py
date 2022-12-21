#Calculating a person's income tax
Income = float(input("Enter your gross income(to the nearest penny) ="))
Dependents = int(input("Enter number of dependents="))
a = Income - 10000 -(Dependents*3000)    #a is the taxable income
tax = a*0.2    #total income tax
if(a>0):
    print("Your income tax =$",tax)
else:
    print("Your income tax = $0")    #If the total taxable income is 0 then the person has 0 income tax
