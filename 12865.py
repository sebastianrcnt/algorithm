itemsCount, maxWeight = input().split()
itemsCount = int(itemsCount)
maxWeight = int(maxWeight)

items = []

for i in range(itemsCount):
  weight, value = input().split()
  weight = int(weight)
  value = int(value)
  valueByWeight = value / weight
  items.append((weight, value, valueByWeight))

items.sort(key=lambda x: x[2], reverse=True)

totalWeight = 0
totalValue = 0

for item in items:
  if totalWeight >= maxWeight:
    break
  if item[0] > maxWeight:
    continue
  totalWeight += item[0]
  totalValue += item[1]

from pprint import pprint
pprint(items)

print(totalValue)

# numberOfItems = 0 ~ 10
# 