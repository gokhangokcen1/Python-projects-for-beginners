import time
information = []
#The specified username and password are stored here

print("\n" + "*"*35)
print("""Welcome to Sign up page
""")

sys_username = input("Choose a username: ")
sys_pass = input("Choose a password: ")
print("\n YOUR REGISTRATION IS COMPLETE\n" + "*"*35)

information.append(sys_username)
information.append(sys_pass)

input_right = 3
#If the information is entered incorrectly 3 times, the code will stop.

print("\nWelcome to Login page")
while True:
    username = input("\nEnter the username: ")
    password = input("Enter the password: ")

    if username not in information and password in information:
        print("**Username is wrong...**")
        input_right -=1
        print("Your right to enter incorrectly: ", input_right)

    elif username in information and password not in information:
        print("**Password is wrong...**")
        input_right -=1
        print("Your right to enter incorrectly: ", input_right)

    elif username not in information and password not in information:
        print("**Username and Password are wrong...**")
        input_right -=1
        print("Your right to enter incorrectly: " , input_right)

    else:
        print("\nYou have successfully logged in.\n")
        time.sleep(0.5)
        print("You are being directed to the site.")
        time.sleep(0.5)
        print("Instagram: @gkngokcen")
        time.sleep(1.5)
        break

    if input_right ==0:
        print("\nYour right to login is over.")
        time.sleep(0.5)
        print(" Try again later.\n The code is shuts down...")
        time.sleep(1.5)
        break