from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render

from contact_us.form import ContactForm


def index4(req):
    if req.method == 'POST':
        conform = ContactForm(req.POST)
        if conform.is_valid():
            return HttpResponse("Submitted")
        else:
            return render(req, 'index.html', {'form': conform})
    else:
        cont = ContactForm()
        return render(req, "index.html", {"form": cont})