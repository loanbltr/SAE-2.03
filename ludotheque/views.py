from django.shortcuts import render, HttpResponseRedirect
from .forms import JeuxForm
from . import models
import os
from django.conf import settings
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def indexmain(request):
    liste = list(models.Jeux.objects.all())
    return render(request, "main.html", {"liste": liste})



def check_permissions(request):
    media_root = settings.MEDIA_ROOT
    try:
        test_file_path = os.path.join(media_root, 'test.txt')
        with open(test_file_path, 'w') as test_file:
            test_file.write('test')
        os.remove(test_file_path)
        return HttpResponse('Permissions are OK')
    except Exception as e:
        return HttpResponse(f'Error: {e}')
