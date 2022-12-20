#a
print('<1~50까지의 정수>')
print()
total = 0

i  = 1 #초기식

c = 1#카운트 횟수 변수


while i<=50 : #조건식

    if c%10 == 0: #한줄에 10개의 숫자
        print(i)

    else: #10개의 숫자가 아니면
        print(i, end = " ")
    
    total += i
    
    i += 1 #증가식
    c+=1
else :
    print("\n%d을(를) 초과하였습니다."%i)

print('\n 1~50까지의 합계는 %d 입니다.' %total)
print()

#1~100까지 4의 배수 - while문

total = 0

i = 4
c = 4
while i <=100:
    if c%7 == 0:
        print(i)

    else :
        print(i, end = " ")

    total += i

    i +=4
    c += 4
else :
    print('\n%d를 초과하였습니다.'%i)

print('\n 1~100까지의 4의 배수 합계는 %d입니다.'%i)
    
    
