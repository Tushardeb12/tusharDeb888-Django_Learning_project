from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import Pagevisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *callback_args, **callback_kwargs):

    qs = Pagevisit.objects.all()

    page_qs = Pagevisit.objects.filter(path = request.path)
    my_title = "I can change u"
    my_context = {
        "page_title": my_title,
        "total_page_visit": qs.count(),
        "page_visit": page_qs.count(),
    }
    path = request.path

    # html_template = "base.html"
    Pagevisit.objects.create(path = request.path)
    # can't pass my_title directly
    return render(request, "home.html", my_context)

def about_view(request, *callback_args, **callback_kwargs):

    qs = Pagevisit.objects.all()

    page_qs = Pagevisit.objects.filter(path = request.path)
    my_title = "I can change u"
    my_context = {
        "page_title": my_title,
        "total_page_visit": qs.count(),
        "page_visit": page_qs.count(),
    }
    path = request.path

    # html_template = "base.html"
    Pagevisit.objects.create(path = request.path)
    # can't pass my_title directly
    return render(request, "home.html", my_context)