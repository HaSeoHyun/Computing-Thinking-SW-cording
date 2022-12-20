name = input('이름: ')
grade = float(input('평균 학점:'))
toeic = int(input('토익 점수:'))
print()

if grade >= 3.5 and toeic > 750:
    result = '지원 가능'

else :
 result = '지원 불가능'

print('''{}님,
평균학점 : {}, 토익 점수: {}
(주)성균에 입사 {}합니다.'''
    .format(name, grade, toeic, result))
