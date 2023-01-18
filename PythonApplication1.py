#Lines firstName to westwins are evalutating data types
#gmetrixDomainOne
#12/17/23

from urllib.parse import quote_plus


firstName = "Samantha"
lastName = "Orange" 
print(lastName + ", " + firstName)

price = 3.42
widgets = 7
print("The price of the widget is", price)
print("We have " + str(widgets) + " in stock.")
print(price * widgets)
print(int(price), float(widgets))
print("   ")
east = 92678
west = 29875
eastwins = east > west
westwins= west > east
print ("Eastwins = ", eastwins, "\nWestwins =", westwins)
print("   ")
#Lines regions = to sales[-1] are convert and work with data types
regions = ["North", "South", "East", "West"]
sales = [30000, 20000, 40000, 35000]
employees = ["Alice", "Vera", "Flo", "Mel"]
locations = []

for employee in employees:
    print(employee)

employees.append("Ava")
employees.remove("Flo")
employees.sort()
print("   ")
for employee in employees:
    print(employee)

print("Region: ", regions[0], "Sales: ", sales[0])
print("Region: ", regions[-1], "Sales: ", sales[-1])
#Lines below are operator sequence and selection

print("   ")
a = 15
b = 25
c = 15
d = 20

print(a == b)
print(a == c)
print(a > c)
print(a >= c)
print(a <= b)
print(a != c)

print("    ")
print(a == c and b != c)
print(a == b and b ==c)
print(a == b or b == c)
print(not a == b or b == c)

print("    ")
e = 8
t = 3 

print(e + t)
print(e - t)
print(e * t)
print(e / t)
print(e ** t) #exponent
print(e % t) #modulus (remainder)

print("    ")
o = 3
g = o 

northItems = ["Rain gear", "Snow shoes"]
eastItems = ["Rain gear", "Snow shoes"]

print(o == g)
print(o is g) #If o changes, so will g. but if northItems changes, eastItems will stay the same .
print(northItems == eastItems) #equal but not dependant. which is why print(northItems is eastItems) is false
print(northItems is eastItems)

print("    ")
newSales = [30000, 32000, 25000, 40000]
quote = "turn could've, would've and should've into can, will, and do."

print(25000 in newSales) #used to say, does the variable cantain this item? answers with t/f
print("do" in quote) #is the word "do" in the quote variable?
print("did" in quote)
