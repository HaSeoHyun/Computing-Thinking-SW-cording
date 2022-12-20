print("<구구단 출력>")

for dan in range (1,10,1):

    for i in range(2,10,1):


        print("%dX%d=%d"%(i, dan, dan * i), end = "  ")
        if i >=9:
            print()
