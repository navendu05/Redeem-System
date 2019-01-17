def calcEMI(L, i, n):
    i=i/12
    M = (L * i * (1 + i) ** n) / ((1 + i) **n - 1)
    return round(M,2)


loan = ["Personal", "Education", "Home", "Car", "Gold"]
print("Hey, Welcome to NAV Bank!\n")
name = input("Please enter your name: ")
print("Hello %s! Here is the list of loan we have:\n" % name)

for count, item in enumerate(loan, 1):
    print(count, item)
c= True
while c:
    type_of_loan = int(input("Loan Type: Please select the loan you want from the above list: "))
    if type_of_loan>0 and type_of_loan<6:
        print("you selected %s loan\n" % loan[type_of_loan - 1])
        c = False
    else:
        print("You have entered a wrong input. ")


if (type_of_loan == 1):
    interest_rate = 0.13
elif (type_of_loan == 2):
    interest_rate = 0.1
elif (type_of_loan == 3):
    interest_rate = 0.06
elif (type_of_loan == 4):
    interest_rate = 0.08
else:
    interest_rate = 0.11

loan_amount = int(input("Please enter the loan amount: "))
loan_tenure = int(input("Please enter the tenure (In Months): "))

emi = calcEMI(loan_amount, interest_rate, loan_tenure)

print("\nLoan Summary:")
print("---------------------------------")
print("Applicant Name: %s\n" % name)
print("Loan Type: %s loan\n" % loan[type_of_loan - 1])
print("Loan Amount: %s Rs\n" % loan_amount)
print("Loan Tenure: %s Months\n" % loan_tenure)
print("Interest Rate: %r\n"%interest_rate )
print("EMI: %s Per Month\n" % emi)
print("---------------------------------")


