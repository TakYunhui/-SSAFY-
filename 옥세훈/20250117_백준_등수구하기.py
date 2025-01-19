n, new, p = map(int, input().split())

if n > 0:
  arr = sorted(list(map(int, input().split())), reverse=True)
    
  rank = 0

  if arr[-1] >= new and n == p:
    print(-1)

  # new가 들어갈 자리가 있을 때
  else:

    for i in range(n):
      rank += 1
      
      if arr[i] <= new:
        print(rank)
        break

    else:
      print(rank+1)
      
else:
  print(1)