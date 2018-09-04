arr = {1, 2, 3, 4, 1, 2, 2, 3, 1, 2, 2, 2}  # 중괄호로 싸여있으면 set, 즉 집합임.
print(type(arr))
print(arr)  # 중복이 사라진 것을 알 수 있음. set 은 집합.
# print(arr[0]) 이렇게 접근이안됨. 순서가없기때문.
# arr = tuple(arr)
# print(arr[0])  # 이렇게 잠시 튜플화 할 수 는 있음.
# orderd? 원래 입력했던 대로 정리되어잇는 것이 아니다. set 은 그렇다는 것을 알아야함. 입력한 순서대로 순서가 되어있는지 모른다는 것.
"""현업 활용은?"""
product = ("py", 'java', 'java', 'node', 'py')
product = tuple(set(product))  # set 을 한번 통과시킴으로써 중복을 삭제해버리게됨.
print(product)

