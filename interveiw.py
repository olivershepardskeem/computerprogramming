name = ""
programming_interest = ""
years_of_experience = 0
desired_salary = 0

print("Welcome to this Programming career Interview! If you're a goofy goober go away.")
print("Please answer the following questions to help us understand your qualifications.")
print("\n")

while not name:
    name = input("Q1. What is your full name(it better not be Goofy Goober)? ")
    if name == "Goofy Goober":
        break

while not programming_interest:
    programming_interest = input("Q2. What type of programming are you interested in(goofy goobing isnt a programming interest)? ")
    if programming_interest == "goofy goobing":
        exit("no goofy goobing")
   
while True:
    try:
        years_of_experience = int(input("Q3. How many years of programming experience do you have? "))
        if years_of_experience >= 0:
            break
        else:
            print("Please enter a real number of years you goofy goober.")
    except ValueError:
        print("Please enter a real number you goofy goober.")

desired_salary = input("Q4. What is your desired salary? ")

education = input("Q5. What is your highest level of education? ")

preferred_technologies = input("Q6. Do you have any preferred programming languages? ")

strengths = input("Q7. What do you consider your strengths as a programmer? ")
weaknesses = input("Q8. What do you consider your weaknesses as a programmer? ")

recent_projects = input("Q9. Can you briefly describe your recent programming projects or work experience? ")

career_goals = input("Q10. What are your long-term career goals in the field of programming? ")

print("\n")
print(f"Thank you, {name}, for giving us all your personal information.")
print("Here's all the answers you gave today:")
print(f"1. Full Name: {name}")
print(f"2. Programming Interest: {programming_interest}")
print(f"3. Years of Experience: {years_of_experience} years")
print(f"4. Desired Salary: {desired_salary} USD")
print(f"5. Education: {education}")
print(f"6. Preferred Technologies: {preferred_technologies}")
print(f"7. Strengths as a Programmer: {strengths}")
print(f"8. Weaknesses as a Programmer: {weaknesses}")
print(f"9. Recent Projects/Work Experience: {recent_projects}")
print(f"10. Long-term Career Goals: {career_goals}")

print("\nThank you for sharing all your personal information with us. We will not be getting in touch with you because you're probably a goofy goober.")