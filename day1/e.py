a = 'korea japna'

a = '''korea

       japan'''
print(a)

a = '\t'
print(a)
print('a')

arr = [1, 2, 3, 4, 5, 6, 7]
num = arr[0]
# 여기서 arr 은 리스트를 가리킴.
num = arr[-3]
print(num)

# 함수 len, length 줄인거
size = len(arr)
print(size)

print(max(arr))
print(min(arr))

tot = sum(arr)
print(tot)
print(sum(arr))


# 물론 max 나 min 등을 쓸 때에는 문자열 섞이면안됨. 같은 데이터타입으로, 문자열만으로 있을때에는 가능
# 알파벳 순에서 가장 늦은 순서나 빠른순서를 내놓음.

arr = [1, 2, 3, 4, 4, 5]
print(arr[0])
arr[0] = 9  # 이걸하면 arr 리스트의 0번째에 9라는 값을 넣음.
print(arr)
arr.append(900)  # 점접근으로 객체에 점근함. append 로 추가도 가능(마지막에 추가됨) , 함수의 self 자리에는 뭐 넣는게 아니므로 append 함수도 값은 하나 넣음
print(arr)

arr.append([55, 66])
print(arr)

print(arr[7][1])  # 리스트내에 리스트의 1번째 내용 찾을때

sar = [10, 40, 60, 10, 90]
