from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
import json
# Create your views here.


    # re
def home(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    }
    return HttpResponse(json.dumps(context)) 
