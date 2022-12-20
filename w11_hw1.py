print("학번:2021313690, 이름: 하서현")
print("<절댓값 출력 프로그램>")

a = int(input("숫자 입력: "))

def toAbs(x):
    if x >= 0:
        print("=>절대값: %d"%x)
        return x

    else:
        print("=>절대값: %d"%-x)
        return x

toAbs(a)
