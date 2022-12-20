money = int(input("투입한 돈 : "))
price = int(input("음료수 값 : "))

print("음료수와 잔돈을 받으세요")

change= money - price

owon = change // 500
iwon = (change-500*owon) // 100
rem = change % 100

print("잔돈: %d"%change)
print("\n>500coin : %d개"%owon)
print("\n>100coin : %d개"%iwon)
print("reminder coin : %d원 "%rem)


                  
