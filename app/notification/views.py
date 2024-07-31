from django.http import HttpResponse


def index(request):
    return HttpResponse("Yup, this is the notification service.")
