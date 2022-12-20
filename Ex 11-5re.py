menu = ["딸기라떼", "망고요거트","사하라","크로플","블랙커피"]
price = [3000,4000,3500,5000,2000]

print("<음료 예약 프로그램>")
print("\t*음료 메뉴*")


def drinkMenu():
    for i in range(1,6,1):
        print("\t", i," : ", menu[i-1])

def drinkInfo(menu_num):
    return print("%s의 금액은 %d입니다"%(menu[menu_num-1],price[menu_num - 1]))

drinkMenu()
print()
num = int(input("메뉴 선택 : "))
print()
drinkInfo(num)


