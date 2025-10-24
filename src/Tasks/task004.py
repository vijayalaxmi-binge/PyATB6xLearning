"""Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request
"""
#input API response code
response=int(input("Enter the response code"))

#Check if the response code is succesfull
if response==200:
    print("✅ Passed API Request")
else:
    print("❌ Failed API Request")

