from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the wordle index.")

#grid display is one view. 
# entering texts is one action that should get into action when i have typed 5 letter
#if i found correct ans, it should display YOU WON. 

def grid_display(request):
    return HttpResponse("Youre looking at grid display")

def submission(request):
    return HttpResponse("youre submitting your guess")

def results(request):
    return HttpResponse("youre looking at results")