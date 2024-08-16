from django.http import HttpResponse
from django.shortcuts import render
class TesteView:
    def renderizar(request):
        return render(request,template_name = 'dashboard.html',status = 200)