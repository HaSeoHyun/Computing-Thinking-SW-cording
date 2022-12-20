import op_module as om

a = int(input("첫 번째 정수 입력 : "))

b = int(input("두 번째 정수 입력 : "))

result = om.add(a,b)
print("%d + %d => %d"%(a,b,result))

result = om.div(a,b)
print("%d / %d => %3.2f"%(a,b,result))
