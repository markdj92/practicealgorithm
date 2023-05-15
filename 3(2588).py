import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

a = m//100
b = (m-a*100)//10
c = (m-a*100-b*10)
    
print(n*c)
print(n*b)
print(n*a)
print(n*m)


