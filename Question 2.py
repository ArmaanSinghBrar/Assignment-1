#Calculating a person's income tax
Income = float(input("Enter your gross income(to the nearest penny) ="))
Dependents = int(input("Enter number of dependents="))
taxable_income = Income - 10000 - (Dependents*3000)
tax = taxable_income*0.2    #total income tax
if(taxable_income>0):
    print("Your income tax = $",tax)
else:
    print("Your income tax = $0")    #If the total taxable income is 0 then the person has 0 income tax
