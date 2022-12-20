menu = ["콜라","사이다","식혜","커피","생수"]
price = [700,800,700,600,500]

print("\t==>자판기<==")

for i in range (0,5,1):
    print("\t", menu[i],":",price[i])


money = int(input("\n돈을 투입하세요 : "))

while True:

    select = int(input("\n메뉴 선택(종료 : 0): "))

    if select == 0:
        break

    if price[select-1] > money:
        print("잔액이 부족합니다")

    else :
        print("%s 구입 완료"%menu[select-1])
        money = money - price[select-1]
        print("잔액: %d"%money)


print("잔액 %d원 반환"%money)
print("음료 자판기 프로그램 종료")
