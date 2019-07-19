from math import sqrt

A = input().split(" ")
B = input().split(" ")

Dist = sqrt( (float(B[0])-float(A[0]))**2 + (float(B[1])-float(A[1]))**2)

print(f'{Dist:.4f}')