import time

start = time.time()

print('i => ', end = " ")

i = 3
while True:
    print(i, end = " ")
    i += 3

    if i>50:
        break


end = time.time()

print("\n\nstart time : ", start)
print("end time", end)
