#점수 = score, 등급: grade, 결과: result, 메세지: mess

print('학번: 2021313690, 이름: 하서현')
print('<학점 등급 출력 프로그램>')

score = int(input('점수를 입력하세요:'))

if 95 <=score<=100 :
    grade = 'A+'

elif 90<=score<=94 :
    grade = 'A'

elif 85<=score<=89 :
    grade = 'B+'

elif 80<=score<=84 :
    grade = 'B'

elif 75<=score<=79 :
    grade = 'C+'

elif 70<=score<=74 :
    grade = 'C'

elif 0<=score<70 :
    grade = 'F'

else :
    grade = '에러입니다. 0~100까지의 숫자를 입력하세요.'

print('=> 등급: %s'%grade)
