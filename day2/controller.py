"""
흐름과 흐름제어
선택흐름과 if문 *** 필요
for 문  *** 필요
while 문  *** 필요
break 문과 continue 문 ** 조금쓰이는정도.
pass 문
무한 반복

"""

print('a')
b = '길동'
if(b):  # 세미불린처럼 처리됨. 세미 부울린? -> 0이면 거짓 나머지 숫자는 그냥 참. 문자열 넣어도 그냥 참임.
        # length 가 0 인 문자열은 None 과 같음. 즉 b = '' 일때에는 그냥 아무일도 안일어남. None, False 취급으로 if문 실행안됨.
        # 공백은 공백이라는 문자열이 있는거임.
    print(b)
"""
jumsu = 80

if(jumsu >= 70):
    print("합격입니다.")
else:
    print("불합격입니다.") ... 이렇게 짜는게 썩 좋지않음.
"""
jumsu = 80
result = ''
if(jumsu >= 70):
    result = '합격'
else:
    result = '불합격'

print('당신의 결과는 {}입니다.'.format(result))  # 이렇게 짜는게 더 좋음.

jumsu = 65

grade = ''
if jumsu >= 90:
    grade = '수'
elif jumsu >= 80:
    grade = '우'
elif jumsu >= 70:
    grade = '미'
elif jumsu >= 60:
    grade = '양'
else:
    grade = '가'

print('당신의 평가는 {}입니다'.format(grade))  # 다중 if 문 구조의 예였음.

a = int(input('숫자를 입력하세요 >'))  # int 로 안 덮어씌우면 int 와 str 형태는 하여튼 그렇게 비교 못한다고함.
b = int(input('숫자를 입력하세요 >'))
c = int(input('숫자를 입력하세요 >'))

# 세 수중 가장 큰 값을 구하여라. 다중 if로. 우선 둘을 비교하고 나머지 하나와 비교하는 논리.
if(a > b):  # if 안의 if 도 다중 if.
    if(a > c):
        max_num = a
    else:  # a가 b보다 크지만 c 보다는 작은 경우
        max_num = c
else:  # a < b 이면
    if(b > c):
        max_num = b
    else:  # b가 a보다 크지만 c 보다는 작은경우
        max_num = c
print(max_num)

# 좀 더 파이썬 스러운 것은?

x = (a, b, c)
max_num = max(x)
print(max_num)

##########################

