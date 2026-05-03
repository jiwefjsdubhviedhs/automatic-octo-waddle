import math


print ('What do you want to compute?')
print ("1 - Compute Required Period")
print ("2 - Compute Required Payment Amount")
print ("3 - Compute Required Interest Rate")
Y = input("Type the corresponding number of the option you want to compute: ")

while Y not in ['1', '2', '3']:
    print()
    print("Invalid choice! Please enter 1, 2, or 3.")
    Y = input("Type the corresponding number of the option you want to compute: ")
print()

print ('What is your Annuity Type?')
print ('A – Annuity Immediate (payment at end of period)')
print ('B – Annuity Due (payment at beginning of period)')
Z = input("Type the corresponding letter of the option that corresponds to your Annuity Type: ")

while Z not in ['A', 'B']:
    print()
    print("Invalid choice! Please enter A or B.")
    Z = input("Type the corresponding letter of the option that corresponds to your Annuity Type: ")


print ()

def Required_Period(x,y):
    if x == '1' and y == "A":
        print("You have chosen to compute the Required Period for Annuity Immediate.")
        FV = float(input("Future Value goal (₱): "))
        PMT = float(input("Regular Payment per period (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = n = math.log(1 + (FV * r / PMT)) / math.log(1 + r)
        print()
        print(f"You need {math.ceil(n)} periods to reach ₱{FV:,.2f} with ₱{PMT:,.2f} payments at the beginning of each period.")  
    elif x == '1' and y == "B":
        print("You have chosen to compute the Required Period for Annuity Due.")
        FV = float(input("Future Value goal (₱): "))
        PMT = float(input("Regular Payment per period (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = math.log(1 + (FV * r) / (PMT * (1 + r))) / math.log(1 + r)
        print()
        print(f"You need {math.ceil(n)} periods to reach ₱{FV:,.2f} with ₱{PMT:,.2f} payments at the end of each period.")  


def required_payment(x,y):
    if x == '2' and y == 'A':
        print("You have chosen to compute the Required Payment for Annuity Immediate.")
        FV = float(input("Future Value goal (₱): "))
        r = float(input("Interest Rate (in decimals): "))
        n = float(input("Number of Periods (in years): "))
        # PMT = FV / [((1+r)^n - 1)/r]
        PMT = FV / (((1 + r) ** n - 1) / r)
        print()
        print(f"You need to save ₱{PMT:,.2f} for {math.ceil(n)} periods to reach ₱{FV:,.2f} at {r*100}% interest")  
    elif x == '2' and y == 'B':
         print("You have chosen to compute the Required Payment for Annuity Due.")
         FV = float(input("Future Value goal (₱): "))
         r = float(input("Interest Rate (in decimals): "))
         n = float(input("Number of Periods (in years): "))
         PMT = FV / ((((1 + r) ** n-1) / r) * (1 + r))
         print(f"You need to save ₱{PMT:,.2f} for {math.ceil(n)} periods to reach ₱{FV:,.2f} at {r*100}% interest")
        # PMT = FV / [(((1+r)^n - 1)/r) * (1+r)]

if Y == '1':
    Required_Period(Y,Z)  

elif Y == '2':
    required_payment(Y,Z)
        
