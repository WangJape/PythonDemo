import random


def wjp(n):
    return 5 * n


li = (1, 2, 3, 4, 5, 6)
s = map(wjp, li)
t = list(s)
print(t)
print(__name__)

dir = {1: '建鹏', 2: '江海'}
print(dir)
index = dir.items()
print(index)
index1 = list(index)
print('index1:{}'.format(index1))
print(index1[0][-1])
s = set(index1)
s.add('1111')
print(s)

r = [random.randint(0, 100) for i in range(1000)]
print(r)
for i in range(101):
    print('{}:{}'.format(i, r.count(i)))
dir1 = {}
for i in range(100):
    dir1[i] = r.count(i)

print(dir1)

for i in dir1:
    print('数字{}的出现次数是{}\t'.format(i, dir1[i]))
    if i % 8 == 0:
        print('\n')

print('-----------------------------------------------------------------')

str = '1111111111222222223333333999984465113216841351215649784561230.864531297465132'
rules = ['2', '4', '6', '8']
for i in rules:
    print(i)
    if i in str:
        str = str.replace(i, '*')
print(str)

if __name__ == '__main__':
    print("我是主函数")
