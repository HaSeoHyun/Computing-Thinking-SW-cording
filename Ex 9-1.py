#for문
print('[for문]')
print('<1~100까지의 3의 배수 출력>')

total = 0
for i in range(3,100,3):
    print(i, end = " ")
    total += i

print('\n3의 배수 총합:%d' %total)
    

print('[리스트 사용]')
print('<1~100까지의 3의 배수 출력>')

threelist = []

#3의 배수를 리스트의 요소로 넣기

total = 0
for i in range(3, 100, 3):
    threelist.append(i)

#합계출력

#[]없애기
for data in threelist:
    print(data, end = " ")
    total += data

print(threelist)
print('3의 배수 총합: %d' %total)
