import sys
input = sys.stdin.readline

n = int(input())
# my_list=[]
for _ in range(n):
    num = input()
    count = 0
    result = 0
    for i in num:
        if i == "O":
            count += 1
            result += count #해당 부분을  elif문 안으로 옮겼을 경우에는 결과값이 마지막 테스트케이스에서만 업데이트되고, 이전 테스트 케이스들은 고려되지 않는다.
        elif i == "X":
            count = 0
    print(result) #print문 또한 for문 밖으로 빼주는 것이 아니라 for문 안에 넣어줘야 n만큼의 테스트 케이스를 돌면서 각각의 result값을 뽑아 낼 수 있다.        