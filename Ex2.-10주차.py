total = 0


for i in range(1,21,1):
    print(i, end = " ")
    total += i

    if total>= 150:
        print("\n최초로 150 넘음: %d"%i)
        print("=>1~%d까지의 합계: %d"%(i,total))
        break
