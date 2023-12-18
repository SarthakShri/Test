"""
Q3> Given an array of integers, find the maximum value of an expression obtained by adding parentheses and +, *, /, - signs between the numbers.
ex:
getMax([1,2,4,-9, 6,4]): Int
getMin([1,2,4,-9, 6,4]): Int

"""

def getMax(arr):
  arr.sort(reverse = True)
  n=len(arr)
  ans=1
  for i in range(n):
    if (i == n-3):
      ans+=arr[i]
      continue
    if (i == n-2):
      ans/=arr[i]
      continue
    if (i == n-1):
      ans-=arr[i]
      continue
    ans*=arr[i]
  print(ans)

def getMin(arr):
  arr.sort(reverse = True)
  n=len(arr)
  ans=1
  for i in range(n):
    if (i == n-4):
      ans-=arr[i]
      continue
    if (i == n-3):
      ans+=arr[i]
      continue
    if (i == n-2):
      ans/=arr[i]
      continue
    if (i == n-1):
      ans*=arr[i]
      continue
    ans*=arr[i]
  print(ans)

getMax([1,2,4,-9, 6,4])
getMin([1,2,4,-9, 6,4])
