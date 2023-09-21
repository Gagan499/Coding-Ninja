n = int(input())
for i in range(1, n+1):
  print(1, end="")
  for j in range(2, i+1):
    if j == i:
      print(1, end="")
    else:
      print(2, end="")
  print()