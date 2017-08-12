def URLify(s):
  out = ''
  
  for section in s.split(' '):
    if len(section) == 0:
      pass
    
    out += section + '%20'
    
  # remove extra from end or beginning
  while True:
    if out.startswith('%20'):
      out = out[3:]
    elif out.endswith('%20'):
      out = out[:-3]
    else:
      break
  
  return out

s = 'Mr John Smith    '
print(URLify(s))
