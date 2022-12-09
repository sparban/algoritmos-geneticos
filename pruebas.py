import random

padre2 = 0
padre1 = random.randint(0,20)
while padre1 == padre2 :
    padre2 = random.randint(0,20)

print(padre1, padre2)