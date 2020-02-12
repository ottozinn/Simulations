import random

coin = 0
heads = 0
tails = 0


numFlips = int(input("How many coin flips? "))

for i in range(numFlips):
    coin = random.randint(1,2)
    if (coin == 1):
        heads += 1
    else:
        tails += 1
print(f"heads: {heads}, tails:{tails}")



