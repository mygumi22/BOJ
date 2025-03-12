# 문제링크 https://www.acmicpc.net/problem/10241

import sys

n = int(sys.stdin.readline())
for i in range(n):
  home = 0
  away = 0
  for _ in range(9):
    h, a = map(int, sys.stdin.readline().split())
    home += h
    away += a
  if home == away:
    print('Draw')
  elif home > away:
    print('Yonsei')
  else:
    print('Korea')

  