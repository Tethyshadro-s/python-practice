import random

#print(help(random))

low = 1
high = 100
options = ("Rock","Paper","Scissors")
cards = ["2","3","4","5","6","7","8","9","10","Q","K","A"]

number = random.randint(low,high)
num = random.random()    #prints random floating int between 1 and 0
option = random.choice(options)
random.shuffle(cards)

print(number)
print(num)  
print(option)
print(cards)
