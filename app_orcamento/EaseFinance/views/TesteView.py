from django.http import HttpResponse


class TesteView:
    def renderizar(request):
        return HttpResponse('<h1>Ola mundo!<h1>')