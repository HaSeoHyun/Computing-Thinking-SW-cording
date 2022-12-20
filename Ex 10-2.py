
print('[입력단에 따른 구구단 출력]')


print()

while True:
    dan = int(input('단(dan) 입력: '))

    print('<%d단 출력>'%dan)

    #for ~range 사용
    for i in range(1,10,1):
        print('%d X %d = %2d'%(dan,i,dan*i))

    print('<%d단 출력 완료>'%dan)
    print()

    a = input("계속 실행['Y' or 'y']/종료['N' or 'n'] 입력: ")


    if a == "Y" or a == 'y':
        continue

    elif a == "N" or a == 'n':
        break
    else:
        print("잘못 입력하셨습니다")

print("구구단 출력 프로그램 종료")

    

