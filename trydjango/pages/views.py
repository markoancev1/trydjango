from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "Contact.html", {})


def about_view(request, *args, **kwargs):

    my_context = {
        "my_text": "This is a text",
        'my_number': 123,
        "my_list": [123, 456, 789, 'ABC']
    }

    return render(request, "about.html", my_context)