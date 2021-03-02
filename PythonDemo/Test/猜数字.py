import random

r = random.randint(0, 100)
print(r)
t = 0
while True:
    n = eval(input('请猜数：'))
    t = t + 1
    if n > r:
        print('遗憾,太大了')
        continue
    elif n < r:
        print('遗憾,太小了')
        continue
    else:
        break
print('恭喜你猜对了！')
print('一共输入了{}次'.format(t))
