import datetime

from django.shortcuts import render

# Create your views here.
def about(request):
    data = {}
    data['date'] = str(datetime.datetime.now()).split('.')[0]
    return render(request, 'about.html', data)