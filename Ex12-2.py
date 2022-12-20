
import random as ra

def menu(lunch):
    rice = ['제육덮밥', '김치볶음밥','된장찌개']
    noodle = ['짜장면','쌀국수','칼국수']
    bread = ['와퍼세트','햄치즈샌드위치','페페로니피자']
    etc = ['떡볶이','스파게티','마라샹궈']
    
    if lunch== '밥':
        recom = ra.choice(rice)
    elif lunch== '면':
        recom = ra.choice(noodle)
    elif lunch== '빵' :
        recom = ra.choice(bread)
    else:
        recom= ra.choice(etc)

    return recom

print("점심 메뉴를 추천해드립니다")

while True:
    lunch_menu = input("밥,면,빵 중 입력하세요(종료:0):")
    
    if lunch_menu == '0':
        break

    print("추천메뉴=>",menu(lunch_menu))
