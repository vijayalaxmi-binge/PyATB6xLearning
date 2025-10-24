print("Enter the which test you want to run")
test_type=input("Enter the test type: API, UI, Performnce, Security")

match test_type:
    case "API":
        print("we are running a postman API testcase")
    case "UI":
        print("we are running a Selenium UI testcase")
    case "Performance":
        print("we are running a Performance testcase")
    case "Security":
        print("we are running a Security testcase")
    case _:
        print("Invalid type.")