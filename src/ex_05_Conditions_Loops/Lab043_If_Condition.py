#write a program to take user age and
#let him know if he can go to club
#21

#Logic Building
#step1
#i/p-->age,int
#o/p-->string(result-->can go to club or not)

# Step2 #Rough Logic
"""
age>21-->print can go
age<21-->print cant go

"""

#Step 3 Logic
age=int(input("Enter the age\n"))

if age>=21:
    print("yes, Can go to club")
else:
    print("no Cant go to club")


