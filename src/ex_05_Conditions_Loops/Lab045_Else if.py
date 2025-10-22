# find the positive number is even or Odd
num=int(input("enter the number").strip())
if num>=0:
     if num%2==0:
         print("Even")
     else:
         print("Odd")
else:
        print("Negative number")
 #You can write short one-liner conditions using the ternary operator
if num>=0:
    print("Even" if num%2 ==0 else"Odd")
else:
    print("Negative Number")