import sqlite3
import tkinter
import tkinter.messagebox
import tkinter.ttk


def initialize():
    for row in tree.get_children():
        tree.delete(row)
    infor = [
        ("王建鹏", "男", "23", "董事长", "18931125201", "1143828481"),
        ("aaaaa", "女", "23", "副董事长", "18931125201", "1143828481"),
        ("bbbbb", "女", "23", "秘书", "18931125201", "1143828481"),
        ("11111", "男", "23", "董事长", "18931125201", "1143828481"),
        ("22222", "女", "23", "副董事长", "18931125201", "1143828481"),
        ("33333", "女", "23", "秘书", "18931125201", "1143828481"),
        ("44444", "男", "23", "董事长", "18931125201", "1143828481"),
        ("55555", "女", "23", "副董事长", "18931125201", "1143828481"),
        ("66666", "女", "23", "秘书", "18931125201", "1143828481")
    ]
    try:
        cur.execute('create table people (name,sex,age,department,phone,qq)')
        cur.executemany('insert into people values (?,?,?,?,?,?)', infor)
        conn.commit()
        print('提示：更改行数{}！'.format(cur.rowcount))
    except:
        print("初始信息表已存在！")
    cur.execute('select * from people')
    temp = cur.fetchall()
    print(temp)
    for i in temp:
        tree.insert('', 0, values=i)


def doSql(sqlStr):
    print(sqlStr)
    cur.execute(sqlStr)
    conn.commit()
    print('提示：更改行数{}！'.format(cur.rowcount))


def addInformatin():
    sqlStr = 'insert into people values("' + varName.get() + '","' + varSex.get() + '","' + varAge.get() + '","' + varDepartment.get() + '","' + varPhone.get() + '","' + varQQ.get() + '")'
    doSql(sqlStr)
    cur.execute('select * from people where name = "' + varName.get() + '"')
    temp = cur.fetchall()
    tree.insert('', 0, values=temp[0])


def clearInformatin():
    varName.set('')
    varSex.set('')
    varAge.set('')
    varDepartment.set('')
    varPhone.set('')
    varQQ.set('')


def treeviewClick(event):
    '''try:
        tree.selection()[0]
    except:
        tkinter.messagebox.showinfo("单击无效！")
        return'''
    global select
    select = tree.selection()[0]
    varTree.set(tree.item(select, 'values')[0])
    print('TreeView选中' + varTree.get())


def delectInfmation():
    if varTree.get() == '':
        tkinter.messagebox.showinfo('删除', '未选中删除项\n请双击需要删除的条目！')
        return
    print(select)
    print(varTree.get())
    sqlStr = 'delete from people where name = "' + varTree.get() + '"'
    print(sqlStr)
    doSql(sqlStr)
    tree.delete(select)
    varTree.set('')


root = tkinter.Tk()
varName = tkinter.StringVar(value='')
varSex = tkinter.StringVar(value='男')
varAge = tkinter.StringVar(value='')
varDepartment = tkinter.StringVar(value='')
varPhone = tkinter.StringVar(value='')
varQQ = tkinter.StringVar(value='')
varTree = tkinter.StringVar(value='')
root.title('建鹏通讯簿')
root['height'] = 500
root['width'] = 440
labelName = tkinter.Label(root, text='姓名：')
labelName.place(x=0, y=5, width=80, height=20)
entryName = tkinter.Entry(root, textvariable=varName)
entryName.place(x=100, y=5, width=90, height=20)

labelSex = tkinter.Label(root, text='性别：')
labelSex.place(x=200, y=5, width=80, height=20)
sex = ['男', '女']
comboSex = tkinter.ttk.Combobox(root, values=tuple(sex), textvariable=varSex)
comboSex.place(x=300, y=5, width=90, height=20)

labelAge = tkinter.Label(root, text='年龄：')
labelAge.place(x=0, y=50, width=80, height=20)
entryAge = tkinter.Entry(root, textvariable=varAge)
entryAge.place(x=100, y=50, width=90, height=20)

labelDepartment = tkinter.Label(root, text='部门：')
labelDepartment.place(x=200, y=50, width=80, height=20)
entryDepartment = tkinter.Entry(root, textvariable=varDepartment)
entryDepartment.place(x=300, y=50, width=90, height=20)

labelPhone = tkinter.Label(root, text='电话：')
labelPhone.place(x=0, y=100, width=80, height=20)
entryPhone = tkinter.Entry(root, textvariable=varPhone)
entryPhone.place(x=100, y=100, width=90, height=20)

labelQQ = tkinter.Label(root, text='QQ：')
labelQQ.place(x=200, y=100, width=80, height=20)
entryQQ = tkinter.Entry(root, textvariable=varQQ)
entryQQ.place(x=300, y=100, width=90, height=20)

buttonAdd = tkinter.Button(root, text='添加', command=addInformatin)
buttonAdd.place(x=100, y=150, width=40, height=30)
buttonClear = tkinter.Button(root, text='重置', command=clearInformatin)
buttonClear.place(x=300, y=150, width=40, height=30)

infView = tkinter.ttk.Treeview(root)
infView.place(x=10, y=200, width=420, height=200)
scrollBar = tkinter.ttk.Scrollbar(infView)
scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tree = tkinter.ttk.Treeview(infView, columns=('name', 'sex', 'age', 'department', 'phone', 'qq'),
                            show="headings", yscrollcommand=scrollBar.set)
tree.column('name', width=55, anchor='center')
tree.column('sex', width=40, anchor='center')
tree.column('age', width=40, anchor='center')
tree.column('department', width=75, anchor='center')
tree.column('phone', width=100, anchor='center')
tree.column('qq', width=90, anchor='center')
tree.heading('name', text='姓名')
tree.heading('sex', text='性别')
tree.heading('age', text='年龄')
tree.heading('department', text='部门')
tree.heading('phone', text='电话')
tree.heading('qq', text='QQ')
tree.bind('<Double-Button-1>', treeviewClick)
tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
scrollBar.config(command=tree.yview)
conn = sqlite3.connect('wjp')
cur = conn.cursor()
try:
    cur.execute('select * from people')
    temp = cur.fetchall()
    for i in temp:
        tree.insert('', 0, values=i)
except:
    initialize()
    print("通讯簿自动初始化！")

buttonInit = tkinter.Button(root, text='初始化', command=initialize)
buttonInit.place(x=20, y=410, width=50, height=30)
buttonSearch = tkinter.Button(root, text='搜索', command=clearInformatin)
buttonSearch.place(x=200, y=410, width=50, height=30)
buttonSearch = tkinter.Button(root, text='删除', command=delectInfmation)
buttonSearch.place(x=370, y=410, width=50, height=30)

varSql = tkinter.StringVar(value='')


def superMan():
    doSql(varSqlEntry.get())
    tempString = "已执行SQL语句：" + varSqlEntry.get()
    varSql.set(tempString)
    for row in tree.get_children():
        tree.delete(row)
    try:
        cur.execute('select * from people')
        temp = cur.fetchall()
        print(temp)
        for i in temp:
            tree.insert('', 0, values=i)
    except:
        temp = '查询错误！'
    print(temp)
    # drop table people


varSqlEntry = tkinter.Entry(root, textvariable=varSql)
varSqlEntry.place(x=10, y=460, width=300, height=30)
buttonSearch = tkinter.Button(root, text='手动执行SQL命令', command=superMan)
buttonSearch.place(x=330, y=460, width=100, height=30)

root.mainloop()
