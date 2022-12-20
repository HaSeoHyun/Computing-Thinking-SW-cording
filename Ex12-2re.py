import random

rice = ["제육덮밥", "김치볶음밥", "된장찌개"]
noodle = ["짜장면", "쌀국수", "칼국수"]
bread = ["와퍼세트', '햄치즈샌드위치", "페페로니 피자"]
etc = ["떡볶이", "스파게티", "마라탕"]

def menu(a):
    return random.choice(a)

print("점심 메뉴를 추천해드립니다.")
lunch_menu = input("밥, 면, 빵 중 입력하세요 : ")

if lunch_menu == "밥":
    lunch_menu = rice

elif lunch_menu == "면":
    lunch_menu = noodle

elif lunch_menu == "빵":
    lunch_menu == bread

else:
    lunch_menu = etc

result = menu(lunch_menu)
print()
print("추천 메뉴 => ",result)
