password = input("Enter your password: ")
 
if password == "":
    print("You didn't enter a password!")
elif len(password) < 6:
    print("Weak password! ❌")
else:
    print("Good password! ✅")