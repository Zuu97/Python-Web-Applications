from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

tasks = ["ML", "DL", "AI"]

def todo_list(request):   
    return render(request, "tasks/todo.html", {
            "tasks":tasks
    })

def create(request):   
    return render(request, "tasks/create.html")
