print("학번: 2021313690, 이름: 하서현")
print("<홀수/짝수 판별 프로그램>")
print()

total = 0


while True:

    num = int(input(">>> 양의 정수 입력: "))
    print()


    if num>0:

        if num % 2 == 0:
            print("입력한 정수는 짝수")

        else:
            print("입력한 정수는 홀수")
        total +=1
        
        choice = input("계속 실행하시겠습니까? (계속: enter, 종료: 0) : ")


        if choice == "0":
        
            print("반복 횟수: %d회"%total)
            
            break
        
        else:
            print()
            continue
        


    else:
        print("입력한 정수 %d는 양의 정수가 아닙니다."%num)
        print("=>양의 정수를 입력하세요")

print("짝수/홀수 판별 프로그램 종료")

