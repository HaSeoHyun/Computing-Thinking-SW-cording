def swap1(x,y):
    x,y = y,x
    print("함수 내부 : x = %d, y = %d"%(x,y))
    print("함수 내부 : a = %d, b = %d"%(a,b))

a = int(input("정수1 입력 : "))
b = int(input("정수2 입력 : "))

    
print("함수 호출 전 : a = %d, b = %d"%(a,b))

print("swap실시")

swap1(a,b)

print("함수 호출 후 : a = %d, b = %d"%(a,b))

