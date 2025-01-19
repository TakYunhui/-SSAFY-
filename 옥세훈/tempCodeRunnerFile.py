n, new, p = map(int, input().split())

if n > 0:
  arr = sorted(list(map(int, input().split())), reverse=True)
    
  rank = 0

  # 마지막 점수가 타겟보다 같거나 크고, 랭크자리가 비었을 때 n + 1
  if arr[-1] >= new and n < p:
    if arr[-1] == new:
      print(n)
    else:
      print(n+1)

  # 마지막 점수가 타겟보다 같거나 크고, 랭크자리가 없을때
  elif arr[-1] >= new and n >= p:
    print(-1)

  # new가 들어갈 자리가 있을 때
  elif arr[-1] < new:

    for i in range(n):
      rank += 1

      # 그 수를 처음 만났을 때 바로 반응하니까, 따로 뭐 할 필요 없잖아?
      if arr[i] <= new:
        print(rank)
        break
      
else:
  print(1)