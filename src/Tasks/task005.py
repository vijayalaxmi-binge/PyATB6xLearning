"""In automation, you often compare expected and actual outputs.
Write code to check if a In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches


True - why >  Strip and convert them into the lowercase = both of them are equal.

"""

expected_title = "Dashboard"
actual_title = "Dashboard "

if expected_title.strip()==actual_title.strip():
    print("Passed API resuest")
else:
    print("Failed API request ")


expected_title = "Dashboard"
actual_title = "dashboard "

if expected_title.strip().lower()==actual_title.strip().lower() :
    print("Passed API resuest")
else:
    print("Failed API request ")

