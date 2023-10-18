from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(
        request,
        "recipes/home.html",
        context={
            "name": "Daniel Estevão",
        },
    )


def sobre(request):
    return render(request, "temp/temp.html")


def contato(request):
    return HttpResponse("CONTATO")
