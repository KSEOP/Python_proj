# while 은 조건이옴. 참인 범위 내에서 계속 반복하다가 거짓이되는 순간 멈춤.
# 1부터 n 까지의 합을 구하는데 100이 넘어가는 n값을 구하여라.

tot = 0
num = 1
while tot <= 100:
    tot += num
    num += 1

print(num, tot)

# break 문과 continue 문
"""
break:  현재 수행중인 반복문 탈출, 다음 단계 수행

continue: 반복문에서 남은 문장을 수행하지 않고 다음 단계로 넘어감
"""

for a in range(1,11):
    if a == 5:
        break  # a가 5일때 if를 탈출해버리므로 5는 출력되지 않음.
    print(a)

for a in range(1, 11):
    if a == 5:
        continue  # a = 5 일때 더이상 수행하지 않음 = 건너 뛰어버림
    print(a)  # 5일 때만 건너 뛰므로 5를 제외한 1부터 10까지 출력됨.


while True:
    if tot >= 100:
        break
    num += 1
    tot += num  # 이 코드는 break 참고용 좋지않음. while 만 쓴게 더좋음.
""" 즉 break 와 continue 는 반복문을 제어하는 용도, if 랑 쓴다고 생각한다는 것은 부적절"""

