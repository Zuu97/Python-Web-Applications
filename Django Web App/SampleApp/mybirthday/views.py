from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

def check_birth(request, month, day):   
    
    current_time = datetime.datetime.now()
    mybirthday =  (current_time.month == int(month)) and (current_time.day == int(day))

    return render(request, 
                  'mybirthday/birthday.html',
                  {'mybirthday' : mybirthday}
                )