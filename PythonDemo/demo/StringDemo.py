import time

if __name__ == '__main__':
    s = """abcde12345"""

    # 切片：[起始位置：结束位置：步进值]（步进值为-1则为反转字符串）
    s1 = s[::-1]
    print(s1)

    print(s + '1')  # 连接
    print(s * 2)  # 重复

    print(r'a\nb')  # 'r/R' 去除转义,原样输出

    print('a' in s)  # True
    print('a' not in s)  # False

    for i in range(10000):
        print('\r' + "原地刷新：" + str(i), end='', flush=True)
        time.sleep(1)
    print()
