import numpy
N, M = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for _ in range(N)])
b = numpy.array([list(map(int, input().split())) for _ in range(N)])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
