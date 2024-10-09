from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenidos")
def healthCheck(request):
    return HttpResponse("ok")