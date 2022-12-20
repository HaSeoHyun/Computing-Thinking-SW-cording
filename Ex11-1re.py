def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


a = int(input("첫 번째 정수 : "))
b = int(input("두 번째 정수 : "))

result = add(a,b)
print("%d + %d = %d"%(a,b,result))

result = div(a,b)
print("%d %% %d = %d"%(a,b,result))
