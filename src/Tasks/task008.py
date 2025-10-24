"""Given a number you need to calculate the factorial of that number
n = 5
Fact = 5×4×3*2*1 = 120
Fact = 0 → 1,
"""
n=5
fact=1
for i in range(1,n+1):
    fact *= i
print(fact)

