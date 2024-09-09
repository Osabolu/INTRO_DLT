from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def bio(request):
    context = {
        "my_intro": "Hey! I'm McCoy, and I'm studying at SQI. "
        "My tutor's name is Winnie, she has a great smile and very patient with her students. "
        "I'm from Edo state, but I lived most of my life in the north; and 'YES' I speak a little hausa."
    } 
    return render(request, "dtl/intro.html", context)
