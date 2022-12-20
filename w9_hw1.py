print('학번: 2021313690, 이름: 하서현')
print()
print('<3의 배수와 곱셈 출력>')
print()

#시작

total = 1

for i in range(3,51,3):
    print(i, end = " ")
    total *= i


print()


print()
print('1~50까지 3의 배수 곱셈 결과')
print('=> %d'%total)
