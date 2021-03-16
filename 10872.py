i = int(input())

def factorial(x):
  res = 1

  if x == 0:
    return 1

  for k in range(1, x + 1):
    res = res * k
  
  return res

print(factorial(i))