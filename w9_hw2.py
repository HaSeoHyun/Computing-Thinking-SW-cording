
numlist = []
total = 0

print('학번: 2021313690, 이름: 하서현\n')

print('<(주)성균 소프트웨어 코딩 자격증 취득 판별>')

print('5과목의 점수를 입력하세요.')

for i in range(5):
    c=i+1
    topic = int(input('%d과목 점수:'%c))
    total += topic
    numlist.append(topic)

#리스트 길이=a, 평균=ave

a = len(numlist)
ave = total / a


print("\n입력한 점수 =>" ,end =" ")
for i in range(len(numlist)):
    print(numlist[i],end = " ")


print('\n \n총점: %d, 평균: %.1f'%(total,ave))

if ave >= 60:     #4
    print('자격등 취득 결과 : 합격')

else:
    print('자격증 취득 결과 : 불합격')
