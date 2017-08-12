def oneAway(string1, string2):
  # sanity check
  if abs(len(string1) - len(string2)) > 1:
    return False
    
  # counters for each string, diff to store # different
  i = 0
  j = 0
  diff = 0
  
  # iterate across both
  while i < len(string1) and j < len(string2):
    # if equal, advance both counters
    if string1[i] == string2[j]:
      i += 1
      j += 1
    
    # if not, advance first counter and add 1 to diff
    else:
      if len(string1) > len(string2):
        i += 1
      elif len(string2) > len(string1):
        j += 1
      else:
        i += 1
        j += 1
      diff += 1
    
    # false if more than one away
    if j > i + 1:
      return False
  
  if diff > 1:
    return False
  else:
    return True
  
str1 = input('str1: ')
str2 = input('str2: ')

print(oneAway(str1, str2))
