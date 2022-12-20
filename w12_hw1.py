print("이름: 하서현, 학번: 2021313690")
print()
print("<홀수/짝수 게임>")

import random

def ras():  # 1번 랜덤 사용자 정의 함수-매개변수 없음
        c = random.randint(1,100)
        return c   #반환값 있음

win = 0 #승리한 횟수입니다

i = 0  #전체 횟수입니다

def compare(a):   # 2번 홀짝 짐작 맞는지 비교-매개변수 있음
        
        if a % 2 == 1 and user == 1 or a % 2 == 0 and user == 2:
                global win
                win += 1
                message = "=>정답!"
                return ("<%d회> %s (컴퓨터 생성 숫자 : %d)")%(i, message, a)              

        elif user == 0:
                message = "끝!"
                return message  #반환값
 
        else:
                message = "=>땡!"
                return ("<%d회> %s (컴퓨터 생성 숫자 : %d)")%(i, message, a)


def result(a,b):    #승률 계산 사용자 정의 함수
        return a / b * 100

while True:
        print("컴퓨터가 1~100까지의 숫자 중 하나의 정수를 생성하였습니다.")
        print()  #밑에 정수형으로 입력 받은거 있음
        user = int(input("홀수[1]/짝수[2] 선택(종료:0)=>")) 
        
        if user == 1 or user == 2:
             
                i +=1
                print(compare(ras()))   #게임을 하자 게임을 하자
                print()
                
        else:               #종료 하자
                print("\t끝!")
   
                print(">>>%d회 중 %d번 승리(승률: %.2f %%)"%(i, win, result(win,i)))
                break


