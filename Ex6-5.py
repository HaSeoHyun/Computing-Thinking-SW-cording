#사전만들기
mydict = {'사과': 'apple', '귤': 'orange','배': 'pear' , '바나나' :'banana'
,'체리':'cherry'}

#사전 출력
print('\t<과일 이름 한영사전>')
print('1. 초기값\n', mydict)
print('-'*55)

#귤 뭐지

print('2. 귤의 영어 단어:' , mydict['귤']) 

#귤은 오렌지가 아님
mydict['귤'] = 'tangerine'
print('3. 수정 후 귤의 영어 단어:',mydict)

#바나나 삭제
del mydict['바나나']
print('4. 바나나 삭제 \n', mydict)

#귤 살제
del mydict['귤']
print('5. 귤 삭제 \n', mydict)
