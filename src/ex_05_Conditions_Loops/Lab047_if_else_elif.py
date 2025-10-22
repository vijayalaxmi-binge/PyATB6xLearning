#Problem find the maximum number between 3 integers

#Logic building
#User inputs-->num1,num2,num3
#O/p-->int or string with mx number

num1=int(input("Enter the first num1\n"))           #5, #10
num2=int(input("Enter the second number num2\n"))  #3, #12
num3=int(input("Enter the third number num3\n"))   #2, #11
   #5>3 AND 5>2 --->5
   #num1->num2 and num1>num3-->num1
   #num2->num1 and num2>num3-->num2
   #num3-max

if num1>=num2 and num1>=num3:
    print("Maximum",num1)
elif num2>=num3 and num2>=num1:
    print("Maximum",num2)
else:
    print("Maximum",num3)
