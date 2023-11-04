from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """
    Home page
    :param request:
    :return:
    """
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    """
    About page
    :param request:
    :return:
    """
    return HttpResponse('<h1>Blog About page</h1>')