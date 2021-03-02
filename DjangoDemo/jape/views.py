from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    import datetime
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")

    # render会读取templates目录下的index.html文件的内容并且用字典中的ctime的值替换模版中的{{ ctime }}
    return render(request, "index.html", {"ctime": ctime})


def hello(request):
    return HttpResponse("返回数据HelloWord")
