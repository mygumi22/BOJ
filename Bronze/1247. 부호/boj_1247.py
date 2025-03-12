# 문제링크 https://www.acmicpc.net/problem/1247

i = 0
S = []

def check_sign(N):
  s = int(0)
  for j in range(N):
    n = int(input())
    s += n
  if s == 0:
    S.append('0')
  elif s > 0:
    S.append('+')
  else:
    S.append('-')
   
while (i < 3):
  i += 1
  N = int(input())
  check_sign(N)

print(*S, sep='\n')