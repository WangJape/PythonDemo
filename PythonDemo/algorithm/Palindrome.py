n = input("输入一个五位数：")
n1 = n[::-1]  # 反转
if n == n1:
    print("是回文")
else:
    print("不是回文")
