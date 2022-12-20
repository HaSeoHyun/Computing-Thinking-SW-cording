print('1. for문')
total = 0
for i in range(1,21,1):
    total += i
    print('i= %d, total=%d'%(i, total))

print('또는')
print('1. while 문')
total = 0
i = 1
while i<21:
    total += i
    print('i= %d, total=%d'%(i, total))
    i +=1
