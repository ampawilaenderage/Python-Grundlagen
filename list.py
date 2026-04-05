import random
emptList = []
numberList = [23,56,13,67,22]
smallList = [1,2,3]
emptList = smallList

print(emptList)
numberList.append(200)
print(22 in numberList)

def new_func(smallList):
    numberList.extend(smallList)
    print(numberList)

new_func(smallList)       

numberList.reverse()
print(numberList)

numberList[0] = 5000
print(numberList)

numberList.remove(1)
print(numberList)

numberList.pop(2)
print(numberList)

print(f'Get Item ',{numberList.__getitem__(4)})
numberList.sort(reverse=False)
print(numberList)

randomList = [random.randint(1, 100) for c in range(20)]
print(randomList)

random.shuffle(randomList)
print(randomList)

randomList = random.sample(randomList,k=3,)
print(randomList)

randomList = [i*i for i in randomList]
print(randomList)

randomList.extend([1,2,3])
print(randomList)

randomList += [222,333,444]
print(randomList)
try:
    randomList.remove(111)
except Exception as e:
    print(e)
print(randomList[-2])
print(randomList[2] - randomList[4])

print(randomList)

for i in randomList:
    print(i)

for i in range(len(randomList)):
    print(randomList[i])