User_name="Ruhan189"
Password="Ruhan@ruhan"
username=input("Enter your username:")
password=input("Enter your password: ")
if username==User_name and password==Password:
    print("Login Successful")
elif username!=User_name and password==Password:
    print("Invalid Username")
elif username==User_name and password!=Password:
    print("Invalid Password")
else:
    print("Invalid Username and Password")

# I have created this smart login system.
