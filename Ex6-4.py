#생성
mydict = {'사과': 'apple', '귤': 'tangerine', '배': 'pear' }

print('\t<과일 이름 한영 사전>\n')

#초기값
print('1. 초기값:', mydict)
print('-'*60)

#바나나 체리 추가
mydict['바나나'] = 'banana'
print('2.바나나 추가\n', mydict)

mydict['체리']= 'cherry'
print('3.체리 추가\n', mydict)

#print('귤:', mydict['귤'])

#한글만
'''hangle = list(mydict.keys())
print("\n4. 한글 단어 목록:", hangle)'''
print("\n4. 한글 단어 목록:", list(mydict.keys()))

#몇개?
'''cnt=len(mydict)
print("\n5. 한영사전 과일 이름 개수: %d개"%cnt)'''
print("\n5. 한영사전 과일 이름 개수:",len(mydict))
