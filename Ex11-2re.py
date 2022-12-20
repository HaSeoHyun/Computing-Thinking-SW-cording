a = int(input("1과목 점수: "))
b = int(input("2과목 점수: "))
c = int(input("3과목 점수: "))

def get_sum(x,y,z):
    return x + y + z

def get_ave(x,y,z):
    return (x+y+z)/3

result = get_sum(a,b,c)

print("합계 : %d "%result)

result = get_ave(a,b,c)
print("평균 : %d"%result)
