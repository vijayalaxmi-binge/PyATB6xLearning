#Grade Calculator
#write a program that calculates and displays the letter grade
#for given numerical score(e.g, A,B,C,D or F)
#Based on the following grading scale

#A:90-100
#B:80-89
#C:70-79
#D:60-69
#F:0-59

#Logic building formula
#1-->i/p-->user input-->score int
#2->o/p-->str, A,B

score=int(input("Enter the score").strip())

if score>100 or score<=-1:
    print("you are a super man!! you cant get a grade")
else:
    if score>=90 and score<=100:
        print("your grade is A")
    elif score>=80 and score<=89:
        print("your grade is B")
    elif score>=70 and score<=79:
        print("your grade is C")
    elif score>=60 and score<=69:
        print("your grade is D")
    else:
        print("Your grade is F")


#float,abc---have to handle in try catch block