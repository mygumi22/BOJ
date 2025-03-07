# 문제링크 https://www.acmicpc.net/problem/24061

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = 0
R = []

def merge_sort(A, low, high):
  if low < high:
    mid = (low + high) // 2
    merge_sort(A, low, mid)
    merge_sort(A, mid + 1, high)
    merge(A, low, mid, high)


def merge(A, low, mid, high):
  global c
  global R
  S = []
  i = low
  j = mid + 1

  while (i <= mid and j <= high):
    if A[i] <= A[j]:
      S.append(A[i])
      i += 1
    else:
      S.append(A[j])
      j += 1
  if i <= mid:
    S += A[i:mid+1]
  elif j <= high:
    S += A[j:high+1]
  for k in range(low, high + 1):
    c += 1
    A[k] = S[k-low]
    if c == K:
      R += A
      
merge_sort(A, 0, len(A) -1)

if (len(R) > 0):
  print(' '.join(str(s) for s in R))
else:
  print('-1')