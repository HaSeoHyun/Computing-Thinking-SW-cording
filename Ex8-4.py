wallet = ['card', 'cash']
myown = input('당신의 지갑에 있는 것은?:')

print()
if myown == 'card' or myown =='cash' :  #또는 if myown in wallet
    trans ='택시를 타고 이동하세요'
else :
    trans = '걸어서 이동하세요'
 
print('지갑에 %s가(이) 있습니다.\n%s'%(myown,trans))
