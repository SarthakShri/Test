"""Q4> Find the lexicographically[Dictionary order] largest string in such a way that a maximum of only two characters positions are changed
Ex: getLexiLargest(“acfgh”) should return hcfga
"""

def  getLexiLargest(word):
  arr=[]
  maxx=-float("inf")
  maxletter , minletter = "" , ""
  for i in word:
    arr.append(ord(i))
  maxx = max(arr)
  minletter = word[0]
  maxletter = chr(maxx)
  ans = ""+maxletter
  for i in range(1,len(word)):
    if word[i] == maxletter:
      ans+=minletter
      continue
    ans+=word[i]
  print(ans)
  

getLexiLargest("acfgh")
getLexiLargest("dbace")
getLexiLargest("hello")
