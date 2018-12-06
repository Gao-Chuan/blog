import datetime
import socket
from django.shortcuts import render


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def index(request):
    data = {}
    # try:
    #     with open('ip', 'r') as f:
    #         ip = f.readline()
    # except:
    #     with open('ip', 'w') as f:
    #         ip = get_host_ip()
    #         f.write(ip)
    ip = '107.182.20.48'
    data['date'] = str(datetime.datetime.now()).split('.')[0]
    return render(request, 'index.html', data)

