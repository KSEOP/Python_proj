"""딕셔너리는 키 값으로 구성되면 접근자체를 '키' 값으로한다. 키값을 index 로 쓰는 것은 권장되지 않는다."""
person = dict(zip(('name', 'age', 'addr'),('ㅇㅇㅇ', 30, 'busan'))) # zip 함수를 이용해서 키 밸류 자체를 리스트이용하는 개념임. 실사용 예 많음.
# person = {'name': '홍길동', 'age': 20, 'addr': 'busan' }  # 디폴트로 일단 Dict 로 인식함.
# print(person['name'])  # 이렇게 키값으로 접근함. -파이썬으로는 이렇게 쓰면되는데
person['name'] = 'ㅇㅇㅇ'  # 딕셔너리는 mutable 임.
# person['sex'] = 1  # 현재 dict 에 있으면 수정이되고 없으면 알아서 추가가 됨.
print(person.get('name'))  # 이렇게 접근도 가능함.  -내부적으로는 이게 발생한다고 여기면됨.
print(person)
print(person.get('sex', 1))  # ,1을 안붙이면 sex 키값이 없으므로 None 이 뜨는데 붙이면 이게 디폴트 value 가됨.
# person = {}
# person['name' ] = ~
# person['age'] = ~
# person['addr'] = ~
# 실제 소스에는 위에처럼 딕셔너리 하나만들고 때려넣는게 더 흔하다고함.

