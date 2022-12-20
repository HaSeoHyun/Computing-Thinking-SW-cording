total = 0
i = 0

while True:
    i +=1
    total += i
    print(i,end = " ")


    if total >= 150:
        print("\n\t최초로 150이 넘는 위치: %d"%i)
        print("총 합: %d"%total)
        break

    

   
    
