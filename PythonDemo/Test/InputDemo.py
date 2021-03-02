def isOdd(num):
    if num % 2 == 1:
        return "Ture"
    else:
        return "False"


n = int(eval(input("输入一个数：")))
c = isOdd(n)
print(c)
