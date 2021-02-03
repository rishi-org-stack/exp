from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
import json
# Create your views here.

def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request,"main.html")
    # re
def home(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    }
    return HttpResponse(json.dumps(context)) 