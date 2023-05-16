import sys
input = sys.stdin.readline

n, x = map(int, input().split())

num = list(map(int, input().split())) #해당 방식은 입력 받은 값을 공백으로 구분하여 정수로 변환 후에 리스트에 저장한다.
# num = []
# for _ in range(n):
#     num.append(map(int, input().split()))
#주석의 방식의 경우에는  입력된 값들을 여러 줄로 받고 각 줄을 리스트로 변환하여 저장하는 방식이다
#만약 내가 리스트안에 수를
#123
#456
#789
#와 같은 방식으로 들어가게 된다.

for i in num:
    if x > i:
        print(i,end=' ') #end 매개변수를 사용하여 출력 끝에 다른 문자열을 추가할 수 있다. 즉, print하는 i요소 뒤에 공백을 추가해 줄 수 있다.
        