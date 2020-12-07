from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'hello/home.html')

def predict(request):
    return HttpResponse("Lets do ML predictions")

#Custom routes with placeholders
def show_input(request, value):        
    return render(request, 
                  'hello/input.html',
                  {
                    "value" : value
                                }
                )