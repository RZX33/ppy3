import random

cities = []
print('Input 10 cities')
i = 0
while i < 10:
    line = input()
    if not line in cities:
        cities.append(line)
        i+=1
    else:
        i-=1
index = 9
while index >= 0:
    number = random.randint(0, index)
    city = cities[number]
    cities.remove(city)
    print(city)
    index-=1


