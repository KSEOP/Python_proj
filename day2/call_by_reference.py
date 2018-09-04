def fun1(a):
    a = 100
    print('a:', a)


num = 10
fun1(num)
print(num)  # fun(num) 넣으면 fun(10) 이고 num = 100 되니까 num 은 100출력되나? 싶었지만 아님
# 애초에 10과 100은 따로있는데 num 과 a가 화살표로 이들을 가리키는 방향만 달라진다고 생각하면 됨.
# 그러니까 def fun1 에서는 num = 10을 참조하여 a 값을 다시 100으로 내놓았을 뿐이지 원래 num 값에 영향을 준 것이 아니므로
# print(num)은 그대로 10을 출력한다.


def fun2(brr):
    print('brr', brr)
    brr[1] = 900
    print('brr', brr)


arr = [1, 2, 3]
fun2(arr)
print(arr)
