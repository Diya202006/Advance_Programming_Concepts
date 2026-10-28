from django.http import HttpResponse


def demo(request):
    return HttpResponse("This is my first Django Project.")
