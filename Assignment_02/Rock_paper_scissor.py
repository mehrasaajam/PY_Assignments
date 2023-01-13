
import random

user_score = 0
computer_score = 0

while computer_score < 3 and user_score < 3:

    user_choise = input("please choise 'rock' or 'paper' or 'scissor': ")
     
    x = random.randint(1, 3)

    if x == 1:
        computer_choise = "rock"

    elif x == 2:
        computer_choise = "paper"

    elif x == 3:
        computer_choise = "scissor"

    print("🧑: ", user_choise)
    print("💻: ", computer_choise)


    if computer_choise == "rock" and user_choise == "paper":
        user_score = user_score+1

    elif computer_choise == "rock" and user_choise == "scissor":
       computer_score = computer_score+1

    elif computer_choise == "paper" and user_choise == "rock":
        computer_score = computer_score+1

    elif computer_choise == "paper" and user_choise == "scissor":
        user_score = user_score+1 

    elif computer_choise == "scissor" and user_choise == "rock":
        user_score = user_score+1

    elif computer_choise == "scissor" and user_choise == "paper":
        computer_score = computer_score+1

    print("user_score=", user_score)
    print("computer_score=", computer_score)

if user_score == 3:
    print("you win 👏")

elif computer_score == 3:
    print("you fail ☹")
