list_ = filter(lambda x: x%2==0, range(1,101))

for i in list_:
    s = ""
    if i % 3 == 0:
        s += "Fizz"
    if i % 5 == 0:
        s += "Buzz"
    if s != "":
        print(i, s)

