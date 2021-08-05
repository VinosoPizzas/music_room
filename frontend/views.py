from django.shortcuts import render

# Create your views here.

#render do frontend, basicamente a integração do react com o django
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')