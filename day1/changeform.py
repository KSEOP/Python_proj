# a = 10
# b = 'korea'
# print( a + b )

a = 3.67
print(a)
"""3.67을 3으로 바꾸고 싶다면?"""
print(int(a))  # 버림하여 내놓음. 반올림안됨. 절삭이라고 함.

a = '100'
b = '200'
print(int(a)+int(b))  # 형변환하여 연산하였음.

a = '100'
b = 200
print( a + str(b))  # str 이 문자열로 바꿔주는거

# print('a = ' + a) a가 정수일때 이렇게 쓰면 오류남. 문자열 + 정수꼴이니까.
# print('a = ', a) 라고 쓰면 괜찮음
print('a =', a, 'b =', b)


