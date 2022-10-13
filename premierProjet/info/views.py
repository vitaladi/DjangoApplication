from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Objectif
# C'est là que nous recueillons les informations dont nous avons besoin pour renvoyer une réponse appropriée.
def index(request):
    # return HttpResponse("Hello world vital!")
    myObjectifs = Objectif.objects.all().values()
    output="+"
    for x in myObjectifs:
        output += x["content"]
    return HttpResponse(output)