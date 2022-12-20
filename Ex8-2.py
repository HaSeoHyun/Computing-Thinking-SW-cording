name = input('이름:')
myid = input('아이디:')
print()

if myid == 'skku' or myid == 'SKKU':
    print('로그인 성공~!!')
    print("환영합니다!!!")
    print("%s님"%name)

else :
    print('로그인 실패 ㅠㅠ')
    print("아이디가 일치하지 않습니다")
    print('%s님'%name)
