# salary = int(input("what is you salary? "))
# years = int(input("how many years have you worked here? "))

# if years >= 5:
#     print(f"Your bonus will be {salary * 0.05}")
# else:
#     print("you do not qualify for a bonus.")




# length = int(input("What is the length of you rectangle? "))

# breadth = int(input("what is the breadth of your rectangle"))

# if length == breadth:
#     print("that is a square.")
# else:
#     print("that is not a square.")

# value_1 = int(input("what is your first number? "))

# value_2 = int(input("what is your second number?"))

# if value_1 >= value_2:
#     print(value_1)
# else: print(value_2)

# ageone = int(input("person one, what is your age?"))
# agetwo = int(input("person two, what is your age?"))
# agethree = int(input("person three, what is your age?"))

# if ageone > agetwo and ageone > agethree:
#     print(ageone)
# elif agetwo > ageone and agetwo > agethree:
#     print(agetwo)
# elif agethree > ageone and agethree > agetwo:
#     print(agethree)

# if ageone < agetwo and ageone < agethree:
#     print(ageone)
# elif agetwo < ageone and agetwo < agethree:
#     print(agetwo)
# elif agethree < ageone and agethree < agetwo:
#     print(agethree)

classheld = int(input("how many classes have been held?"))
classattend = int(input("how many classes have been attended?"))

if classattend / classheld >= 0.75:
    print("you can sit in the exam")
else: print("you cannot sit in the exam")