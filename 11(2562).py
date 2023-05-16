import sys
input = sys.stdin.readline

num_list = []

for _ in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)
#index()함수는 리스트에서 특정 값의 인덱스를 반환하는 함수이다. +1을 해주는 이유는 index의 시작 값은 0부터 시작이기 때문이다.