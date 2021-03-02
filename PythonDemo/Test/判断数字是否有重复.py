def judge(li):
    length1 = len(li)
    sets = set(li)
    length2 = len(sets)
    if length1 != length2:
        return True
    return False


s = input("输入一串元素，我也不知道是用逗号分隔还是咋，反正这个是不用逗号的：")
l1 = list(s)
flag = judge(l1)
print(flag)
# -----------------------------------------------------------------------------
s2 = input("输入一串元素，这一回是用逗号分隔出来：英文逗号中文逗号都行，为什么呢，因为我做了兼容：")
l2 = s2.split(",")
print(l2)
l4 = []
for i in l2:
    l3 = i.split("，")
    for j in l3:
        l4.append(j)
print(l4)
flag = judge(l4)
print(flag)
