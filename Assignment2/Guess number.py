
import random

computer_number = random.randint(0, 100)
your_try_number = 1

for i in range(10):
    user_number = int(input("please inter your guess (an integer) between 0 & 100: "))

    if computer_number == user_number:
        print("you win 🎊")
        print("you win in try", i)
        break
    
    elif computer_number > user_number and i != 9:
        print("go up ↑")

    elif computer_number < user_number and i != 9:
        print("go down ↓")

    if computer_number != user_number and i == 9:
         print("you failed ☹")
 