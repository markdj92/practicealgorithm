import sys
input = sys.stdin.readline

score = []
c = int(input())

for _ in range(c):
    num = list(map(int, input().split())) #num이라는 리스트 안에 인트형으로 숫자들을 넣겠다는 의미이다.
    avg = sum(num[1:])/num[0] #처음에는 리스트에 넣을 숫자 갯수를 정해주고 리스트에 숫자를 넣어주려고 했었다 하지만 그럴 필요없이 내가 원하는 값을 슬라이싱으로 구분하여 받으면된다.
    count = 0
    for i in num[1:]:
        if i > avg:
            count += 1
    rate = count/num[0] * 100 #count값을 이용해서 rate를 표시하였다. 이 부분을 어떻게 표현하는 지 처음에는 생각하지 못해서 헤메었다.
    print(f'{rate:.3f}%')
    
#f스트링에 대해서 알아보자
#f스트링은 문자열 내에 중괄호{}를 사용하여 변수, 표현식, 함수 등을 쉽게 삽입할 수 있게 해준다.
#예를 들어 name = "Alice"
#age = 25
#print(f"My name is {name} and I'm {age} years old.")
#위의 값을 출력하면 My name is Alice and I'm 25 years old.가 출력되게 만든다.
#뒤에 :.3f는 소수점 3자리까지 표현하는 방법이다.
