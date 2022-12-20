print("학번: 2021313690, 이름: 하서현")
print("<inch->cm 출력 프로그램>")
print()

x = float(input("inch 입력:"))


def inchToCenti(x): #매개변수 있음
    
    y = x * 2.54
    
    print("\t =>%.2f cm"%y)
    
    return x #반환값 있음

inchToCenti(y)  #호출
