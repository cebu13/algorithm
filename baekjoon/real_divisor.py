#1037
import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
A.sort()
print(A[0] * A[-1])