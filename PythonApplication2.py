#Domain 2 Flow control with Decisions and Loops
#i hope this works
#Branching Statements
annualSales = 3000
if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000:
    print("Bronze Customer")
else:
    print("Up and Coming Customer")
print("Thank you for your business")

print("    ")

birdSales = 300000
region = "North"

if birdSales >= 500000:
    print("Gold Customer")
elif birdSales >= 300000:
    print("Silver Customer")
    if region == ("North"):
        print("Send a snowboard")
    else:
        print("Send a baseball bat")
elif birdSales >= 100000:
    print("Bronze Customer")
print("Thank you for your business")

print("    ")

catSales = 200000
newCustomer = True

if catSales >= 500000:
    print("Gold Customer")
elif catSales >= 300000:
    print("Silver Customer")
elif catSales >= 100000 and newCustomer:
    print("Bronze Customer and first-time prize winner!")    
elif catSales >= 100000:
     print("Bronze Customer")


print("Thank you for your business")


#Iterations
print("    ")

capitalGuess = input("What is the capital of Latvia? ")
numberOfGuesses = 1

while (capitalGuess != "Riga") and (capitalGuess != "riga"): #While variable is true, or in this case, while capitalGuess is false.
    numberOfGuesses = numberOfGuesses + 1
    capitalGuess = input("Guess again. ")

print("You guessed it. Riga is the capital of Larvia. It took you " + str(numberOfGuesses) + " guesses." )



print("    ")
initalSalesGoal = 20000
multiplier = 100

for monthlyGoal in range(1,13): #A for loop is set to run a certian number of times
    monthlySalesGoal = initalSalesGoal + (monthlyGoal * multiplier)
    print("Your sales goal for the month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))

print("Good luck with your goals! :)")