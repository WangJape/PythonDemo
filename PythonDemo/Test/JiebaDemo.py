# pip install jieba

import jieba

opens = open("红楼梦.txt", "r", encoding='utf-8')
txt = opens.read()
words = jieba.lcut(txt)
exclude = ['什么', '一个', '我们', '那里', '你们', '如今', '说道', '知道',
           '老太太', '起来', '姑娘', '这里', '出来', '他们', '众人']
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '凤姐儿':
        word = '凤姐'
    elif word == '林黛玉' or word == '黛玉道':
        word = '黛玉'
    elif word == '贾宝玉':
        word = '宝玉'
    counts[word] = counts.get(word, 0) + 1
for word in exclude:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    w, c = items[i]
    print("{0:<10}{1:>5}".format(w, c))
