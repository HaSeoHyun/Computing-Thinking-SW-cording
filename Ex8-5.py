userid = input('아이디를 입력하세요:' )

#검증

if userid == 'skku' :
    print('아이디 일치')
    userpw = input('비밀번호를 입력하세요:')
    if userpw == 'python' :
         print('비밀번호 일치')
         print('\n성균이님, 로그인 성공\n환영합니다')
    else :
         print('비밀번호 불일치')

else : print('아이디 불일치')
