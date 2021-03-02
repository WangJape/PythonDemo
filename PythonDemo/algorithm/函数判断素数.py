def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        else:
            i += 1
    if i < n:
        return False
    else:
        return True


while True:
    try:
        num = eval(input("输入一个整数："))
        break
    except:
        print("输入错误！")
s = is_prime(num)
print(s)
