#Input and output Operations

import os

print("thats pretty gay idk")
print("man this sucks")

print("     ")

workFile = open('urizons.txt',"r")
#workFileContents = workFile.read()
#print(workFileContents)
print("     ")

#you can only use one, .read() or .readline() not both or else the second in the sequence wont work
workFileFirstLine = workFile.readline()
print(workFileFirstLine)

workFileSecondLine = workFile.readline()
print(workFileSecondLine)
workFile.close() #make sure to have this *at the end*

if os.path.isfile("urizons.txt"):
    writeFile = open('urizons.txt',"a")
else:
    writeFile = open('urizons.txt',"w")
toLog = input("What do you want to write in the log? ")
writeFile.write("\n" + toLog)
writeFile.close()
