import datetime

from django.shortcuts import render


def list(request):
    data = {}
    data['date'] = str(datetime.datetime.now()).split('.')[0]

    return render(request, 'archives/list.html', data)


def archives(request, name):
    data = {}
    data['date'] = str(datetime.datetime.now()).split('.')[0]
    data['name'] = '洋务运动与明治维新'

    return render(request, 'archives/posts/'+name+'.html', data)
