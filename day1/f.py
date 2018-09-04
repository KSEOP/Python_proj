a = (1, 2, 3, 4, 5)

print(type(a))
print(a[-2])
print(max(a))

a = list(a)  # 이걸쓰면 튜플을 다시 리스트로 만들 수 있음
a[0] = 10
print(a)

a = tuple(a)  # 리스트 수정이 끝났으면 다시 튜플화 시킬수도 있음

brr = 'korea'
print(brr[0])
# brr[0] = 'o' <- 이거 하면 오류남. 문자열은 튜플로 처리되기 때문임.

