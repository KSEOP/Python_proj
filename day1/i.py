# keys = ('a', 'b', 'c', 'd')
# arr = dict.fromkeys(keys, 0)  # value 값을 가져오는함수. 콤마 이용해서 디폴트값 설정가능.
# print(arr)
""" update 와 setdefault """
person = {'name': '홍길동'}
# person.update(addr='pusan')  # 키와 밸류값이 추가됨 없으면 추가하고 있으면 수정됨.
# person.update(addr='seoul')  # 즉 update 는 수정 및 추가임

# person.setdefault('addr', 'pusan')  # 기존에 addr 이 없으니 pusan 이 입력됨
# person.setdefault('addr', 'seoul')  # 이미 addr 이라는 키에 pusan 이라는 value 가 있으므로 작동하지 않는 코드가됨. 즉 있으면 그대로 둠.

# print(person.pop('name')) # pop 하면서 name 에 대한 value 값을 출력하고 name 이라는 키 값은 제거되버림.

# del person['name'] # delete 진짜 그냥 키값을 단순히 지워버림. 옛날 파이썬 방식.

print(person.items())  # dict_items 라는 객체이자 class 임. 리스트아님. 대괄호가 있지만 단독적인 타입임.
# print(list(person.items())) 해야 진짜 리스트임.

# person.clear() 하면 그냥 텅비어버림. 빈 딕셔너리 남음.
print(person)

arr = (1, 2, 3, 4, 5)
print(1 in arr)  # in 은 왼쪽이 오른쪽에 있냐 없냐를 의미함. 불린값을 내놓음.
print(10 not in arr)  # not 이니까 안들어있으면 True 임.

arr = {'a': 0, 'b': 1, 'c': 2 }
print(1 in arr)  # 이경우는 key 값을 보는 것이므로 value 에 1이 있든말든 상관이 없다.

s = 'korea japan usa'
print('japan' in s)  # 됨 문자열 자체가 탐색됨. 대소문자는 구분함.


