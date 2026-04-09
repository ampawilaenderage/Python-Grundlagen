import random


lottoSet = set()
while len(lottoSet) < 6:
    lottoSet.add(random.randint(1, 49))
print(f'LottoZalen (set): {sorted(lottoSet)}')

bigSet = {1000,2000,3500,(1, 2)} 
bigSet.remove(1000) # comes error when 1000 is not in the list
bigSet.discard(1000) # this is the best way
lottoSet.add((1, 2))
bigSet = lottoSet.union(bigSet)

print(lottoSet)
print(bigSet)
print(bigSet.update({55,66}))

print(bigSet)



