# arr = [1, 2, 3, 4, 5, 6, 7]
arr = {'a': 1, 'b': 2, 'c': 'aaa'}  # 딕셔너리도 for 문 접근가능 키값을 일단 내놓음.
for a in arr:
    print(a)  # print(arr[a]) 라고쓰면 값들이 나열됨 하여간 딕셔너리가 for 문으로 가능 하다는 것.

arr = 'korea japan usa dfdsafkjlekf'
result = {}
for aa in arr:
    if result.get(aa) == None :  # result 라는 빈 딕셔너리에서 get(aa)를 통해 aa 한 문자를 가져와야하는데 result 내에 없으면
        result[aa] = 0           # result[aa] : 0 이라는 키 밸류값이 추가됨. 즉 제일 처음에는 k : 0 이 추가되게되고
    result[aa] += 1              # 이 이프문이 종료된 이후에 k += 1 이 되어 k = 1 이됨.
print(result)
# 즉 get 메써드에서 처음 발견된 문자열 하나 aa는 반드시 none 값이고, none 값이면 result[aa] 값을 키로하고 0을 value 로 하는 딕셔너리가 추가됨을 이해하면됨.

arr = [(1, 2), (3, 4), (5, 6)]

for a, b in arr:
    print(a+b)
