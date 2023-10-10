playerone = int(input("Rock, paper or scissors? "))

playertwo = int(input("Rock, paper or scissors? "))

if playerone == "rock" and playertwo == "scissors":
    print("player one wins")

elif playertwo == "rock" and playerone == "scissors":
    print("player one wins")

elif playerone == "scissors" and playertwo == "paper":
    print("player one wins")

elif playertwo == "scissors" and playerone == "paper":
    print("player two wins")

elif playerone == "paper" and playertwo == "rock":
    print("player one wins")

elif playertwo == "paper" and playerone == "rock":
    print("player two wins")

else:
 print("tie")