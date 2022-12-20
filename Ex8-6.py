
import sys #sys를 사용한

print('<홀수/짝수 판별 프로그램>')

#입력
num = int(input('양의 정수를 입력하세요:'))
print()

#처리 및 출력

if num >0: #밑에 전체 드래그해서 탭키: 전체 띄어쓰기 됨
    
    if num%2 == 1:
        result = '홀수'

    else:
        result = '짝수'
else:
    print('양의 정수가 아닙니다.')
    sys.exit() #시스템 종료(import 와 함께 쓰임)

print("입력한 정수 %d : %s"%(num, result))
