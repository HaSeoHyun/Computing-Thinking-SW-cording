print("학번 : 2021313690, 이름: 하서현")
print("-"*35)

#처음

time = int(input("시간입력(초) : "))

#시분초
hour = time//3600

minute = (time - hour*3600)//60

second = time - hour*3600 - minute*60

print('\n=> %d시간 %d분 %d초'%(hour,minute,second))
