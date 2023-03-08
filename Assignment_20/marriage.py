
import random

boy_list = ["ali", "amir", "hasan", "kaveh", "mahdi", "soroosh"]
girl_list = ["mahsa", "neda", "mahgol", "nagar", "noora"]

n = min(len(boy_list), len(girl_list))
result = []

for i in range(n):
    boy = random.choice(boy_list)
    boy_list.remove(boy)
    girl = random.choice(girl_list)
    girl_list.remove(girl)
    result.append((boy, girl))

print("result: ", result)

if len(boy_list) != 0:
    print("remind boy(s): ", boy_list)    
elif len(girl_list) != 0:
    print("remind girl(s): ", girl_list)