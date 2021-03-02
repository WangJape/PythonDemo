# 三阶幻方问题
# 位置关系
# 0 1 2
# 3 4 5
# 6 7 8


def magic3():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = []

    def check(x):
        if x[0] + x[1] + x[2] != 15: return False
        if x[3] + x[4] + x[5] != 15: return False
        if x[6] + x[7] + x[8] != 15: return False
        if x[0] + x[3] + x[6] != 15: return False
        if x[1] + x[4] + x[7] != 15: return False
        if x[2] + x[5] + x[8] != 15: return False
        if x[0] + x[4] + x[8] != 15: return False
        if x[2] + x[4] + x[6] != 15: return False
        return True

    ## 生成全排列的遍历
    def f(x, k):
        if k == len(x) - 1:
            if check(x): r.append(x[:])
            return
        for i in range(k, len(x)):
            x[k], x[i] = x[i], x[k]
            f(x, k + 1)
            x[k], x[i] = x[i], x[k]

    f(a, 0)
    return r


if __name__ == '__main__':
    print(magic3())
