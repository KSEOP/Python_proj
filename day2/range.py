tot = 0
for a in range(1, 11):
    tot += a

print(tot)

# 1부터 10 사이의 ㅜ 중에 3의 배수의 합을 구하여라

tot = 0

for a in range(1, 11):
    if a % 3 == 0:
        tot += a
print(tot)

# 1부터 100사이의 10의 배수의 합
tot = 0
for a in range(1, 101):
    if a % 10 == 0:
        tot += a
print(tot)

# 세 수를 입력받아 첫번째 수와 두번째 수 사이의 수 중에서 세번째 배수의 합만 구하여 출력하라. 과제로 해볼만 한 것.
