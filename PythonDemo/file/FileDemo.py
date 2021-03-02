try:
    file = open('E:\\项目\\b.txt', 'r', encoding="utf-8")
    print(file.encoding)
    data = file.read(1024)
    print(data)
    file.close()
except Exception as e:
    print(e)

try:
    write_file = open('E:\\项目\\a.txt', 'w')
    print(write_file.encoding)
    write_file.write('王建鹏，魏鹏')
    write_file.flush()
    write_file.close()
except (IOError, NameError) as e:
    print("错误" + e)
