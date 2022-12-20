print('학번: 2021313690, 이름: 하서현')
print('장학생 판별 프로그램')

print()
name = input('이름을 입력하세요: ')
print()
print('3과목의 점수를 각각 입력하세요.')
sco1 = float(input('1과목 점수:'))
sco2 = float(input('2과목 점수:'))
sco3 = float(input('3과목 점수: '))

#합계 = hab, 평균= ave, 메세지 = message

hab = sco1 + sco2 + sco3

ave = hab/3

print('\n이름: %s'%name)
print('총점: %.0f, 평균 : %.1f '%(hab, ave))

if ave >= 95:
   message = '결과: 장학생 \n축하합니다!'

else :
   message = '결과 : 학생 \n다음 학기에 도전하세요'
print()
print(message)
