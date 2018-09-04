"""연산자 학습."""

a = 3
b = 2
print(a / b)
print(a // b)
print(a % b)  # 나머지를 구하는 연산자. 음수를 양수로 나누면 나머지는 양수가나옴. 양수를 음수로 나누면 음수가 나옴.

"""

** 거듭제곱
// 나눗셈의 몫을 구함.
%  나눗셈의 나머지를 구함
-  뺼셈

복합연산자

a = 10
a = a + 5 는 누적식이라고 함. 누적식은 본래 값을 변화시킴. 
-> a += 5

a = a - 5
-> a -= 5

"""
# c *= a + b ?  이 경우는 (a+b) 로 적혀있다고 보아야함. 풀어쓰면
# c = c * (a + b)

a = 3
b = 4
c = 2
c *= a + b
print(c)

""" 비교연산자 """
""" 

== 수식의 값이 같음을 평가
!= 값이 같지 않음을 평가
>,< 크고작음을 평가
>= , <= 같거나 큰지, 같거나 작은지 평가

"""

a = [10, 11]
b = [10, 11]
print('비교연산자 테스트', a == b)  # 파이썬은 내용을 비교함. 다른언어에서는 이걸 같지 않다고 한다고 한다.
"""
파이썬에서는 10 <= x <= 100 이런 모양도 지원해줌."""

""" 논리 연산자 and or not """

a = True
b = None  # None 을 넣으면 and 연산자에서 None 만 나옴. a가 True 던 False 던.
print('논리연산자 테스트', a and b)

# 세미불린
a = 0
b = 3
print(a and b)


