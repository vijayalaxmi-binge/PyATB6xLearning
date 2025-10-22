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
age=int(input("Enter the age\n").strip())
#strip() remove the extra spaces from the input function
if age<=0 or age>130:
    print("Enter the valid age")
else:
    if age>=21:
            print("yes, Can go to club")
    else:
            print("no Cant go to club")

#step4:Check for the edge cases
# we should consider edge cases such as:
#negative ages or extremely high values->program will break
#non-numeric input like -ABC
#AGe which is valid.>130


