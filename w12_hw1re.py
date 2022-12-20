import random

def ransel():
    return random. randint(1,100)


print("<홀수/짝수 게임 >")
print("\n컴퓨터가 1~100 중 하나의 정수를 생성하였습니다.")
print()


def compare(a,b):

    if a % 2==0 and b == 2 or a%2==1 and b == 1:        
        print("정답!")

    else:
        print("땡!")

while True :         
    choice = int(input("홀수[1]/짝수[2] 선택(종료:0)=>"))
    print(compare(ransel(),choice))
    

