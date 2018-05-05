from django.conf import settings
from django.shortcuts import render

from MAIN.webpack import webpack_dev_server


# Create your views here.
def index(request):
    return render(request, template_name='ui/index.html', context={ 'settings': settings })
