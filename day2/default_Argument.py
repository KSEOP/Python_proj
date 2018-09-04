"""기본인자란?"""


def fun1(a):
    print(a)


fun1(10)
fun1(20)  # fun(20,30) 이라고 해버리면 받는 인자의 수를 초과하므로 "오버로딩" 이라고 칭함.


def fun2(a, b=900):  # b=None 해도됨. None 도 값임.
    print(a, b)


fun2(10)
