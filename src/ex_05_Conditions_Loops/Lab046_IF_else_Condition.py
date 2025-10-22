#Problem to find the max number between two

#Logic Building formula
#i/p-->USer inputs-->two integers
#O/p-->int 1 which ever is greater that number will return
#31.5, 67.5-->float

num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))

#if num1>=0 and num2>0:
#   print("Number should be positive")


if num1>=num2:
    print("Maximun",num1)
else:
    print("Maximun",num2)