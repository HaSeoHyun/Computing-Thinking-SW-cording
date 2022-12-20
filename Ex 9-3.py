print('<구구단 출력>')
print()

dan = int(input('단(dan) 입력: '))

print('<%d단 출력>'%dan)

#for ~range 사용
for i in range(1,10,1):
    print('%d X %d = %2d'%(dan,i,dan*i))

print('<%d단 출력 완료>'%dan)
print()

#while이용
print()
print('<구구단 출력>')
print()

dan = int(input('단(dan) 입력: '))
print( '<%d단 출력>'%dan)
i=1
while i <=9:
     print('%d X %d = %2d'%(dan,i,dan*i))

     i += 1

else:
    print('<%d단 출력 완료>'%dan)
    

