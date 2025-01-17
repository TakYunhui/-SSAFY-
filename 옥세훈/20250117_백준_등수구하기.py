n, new, p = map(int, input().split())

if n > 0:
  arr = sorted(list(map(int, input().split())), reverse=True)
    
  rank = 0

  for i in range(n):
    rank += 1
    
    if i > p or arr[i] == new:
      break
      
  
  if n < p:
    if arr[-1] >= new:
      print(rank+1)
    else:
      print(rank)
  else:
    if arr[p-1] >= new:
      print(-1)
    else:
      print(rank)
      
    
else:
  print(1)