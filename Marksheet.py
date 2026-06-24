score = float(input("Enter your score: "))

if score > 100 or score < 0:
    print("Invalid score! Enter between 0 and 100.")

elif score > 85:
    print("Grade : A")
    print("Result: Excellent! Keep it up!")

elif score > 65:
    print("Grade : B")
    print("Result: Good job! Room to grow.")

elif score > 35:
    print("Grade : C")
    print("Result: Please work hard!")

else:
    print("Grade : F")
    print("Result: You failed. Don't give up!")