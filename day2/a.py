# list[3][0] -> 리스트의 리스트일때, 3번째(0번째부터 존재함)요소에 있는 리스트의 0번째 component.
""" SLICE 슬라이스, 리스트나 튜플, 스트링 가능"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [a:b:1or-1] a에서 b까지 1은 정순 -1은 역순
b = a[7:3:-1]

# a만 쓰고 콜론의 뒤를 생략하면 끝까지, 그리고 정순. a를 안쓰면 처음부터.
# 즉 처음부터 slice 하려면 [:7] 처럼 첫 공간을 비워놓음. 즉 [:] 이렇게 쓰면 처음부터 끝까지임.
print(b)

b = a[:]
b[3] = 100
print(a)
print(b)  # 이렇게 실행하면 a와 b의 출력값이 다름. 즉 b=a[:] 는 b=a가 아니란말임. 전자는 슬라이스해서 만들어진 새로운 리스트임.

"""id()를 통해서 고유 번호를 알 수 있음."""

# 데이터의 덧셈과 곱셈. 곱셈하면 그 양이 세번 반복됨
# [1,2,3]*3 = [1,2,3,1,2,3,1,2,3]
# print('#'*30) 이런식으로 쓸수있음. 문자열 자체를 곱셈으로 양을 불려버릴 수 있다.

a = ['korea', 'japan', 'usa']
print(min(a))
# a=97 b=98.. A=65 B=66... 으로 그 크기값을 갖고있음. 소문자가 더 크게 판별됨. japan 이 min 인 이유도
# j가 알파벳 순으로 가장 빠르기 때문에 크기값이 min 임.
# print(min(a, key=len ))
