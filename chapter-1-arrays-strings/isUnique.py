def isUnique(s):
  chars = {}
  for c in s:
    if c not in chars:
      chars[c] = 1
    else:
      return False
  return True
  
strtest = input()
print(isUnique(strtest))
