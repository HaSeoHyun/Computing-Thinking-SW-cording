a = int(input("정수를 입력하세요 :"))
b = int(input("정수를 또 입력하세요 : "))

def get_max(x,y):
    if x > y:
        return x
    else:
        return y


def get_min(x,y):
    if x<y:
        return x

    else :
        return y

result= get_max(a,b)
print("최대값 : %d"%result)

result= get_min(a,b)
print("최소값 : %d"%result)
