train = ["명륜","펭수","정은","윤상","성균"]
print("1.부산역 출발:",train)
print("-"*55)

train.remove("명륜")
train.insert(0,"모범")


print("2.대전역 출발:",train)
train.remove("정은")
train.pop(2)


print("3.용산역 출발:",train)

train.sort(reverse=True)
print("-"*55)
print("4.서울역 도착:",train)
