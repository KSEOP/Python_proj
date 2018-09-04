"""함수문법"""
# 파이썬은 무조건 반환값이 있다! 설정안하면 None 값이 기본 반환임.


# 두 수를 입력받아 합을 구하는 함수를 정의하여라

def do_sum(s1, s2):  # 이렇게쓰면 인자를 2개받는 함수가 완성 된 것임.
    x = s1 + s2
    return x, 'korea'  # python 은 return 이 여러개를 반활 할 수 있음.


x, y = 10, 20
a = do_sum(3, 5)
print(a)  # 리턴값이 두개이므로 알아서 두개짜리 튜플로 값이나옴
print(a[0], a[1])  # 튜플 괄호를 벗긴것이 출력됨

"""함수는 반드시 리턴값이 있다."""

"""
def pr():
    pass

a = pr()
print(a)  # 이러면 None 값이나옴.
"""


def pr():
    print('pr')


print(pr())  # return 이 없어도 return None 이 써져있다고 생각하고 컴파일 하는것임

# call by reference
