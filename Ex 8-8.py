#입력

temperature = int(input('현재 온도는:'))

if temperature>15:
    recom = '따뜻합니다. 가벼운 차림'
 
elif 10<temperature<=15:
    recom = '쌀쌀합니다. 가디건 준비'


elif 0<temperature<=10:
    recom = '조금 추워요. 뚜꺼운 외투'


elif temperature<=0:
    recom = '완전 추워요. 따뜻한 패딩'

print('\n현재 온도는 %d도 입니다.'%temperature)
print(recom)
