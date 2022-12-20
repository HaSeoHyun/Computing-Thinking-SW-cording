attend = int(input('출석: '))
quiz = int(input('퀴즈: '))
usual = int(input('평소 학습: '))
assing = int(input('과제: '))
ppt = int(input('발표: '))
final = int(input('기말점수: '))

#처리
total = attend*0.1 + quiz*0.1 + usual*0.3 + assing*0.2 + ppt*0.1 + final*0.2

#출력
print('"컴퓨팅 사고와 SW코딩" 총점 : %.2f'%total)


