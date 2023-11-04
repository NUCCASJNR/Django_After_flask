from django.shortcuts import render



def home(request):
    """
    Home page
    :param request:
    :return:
    """
    return render(request, "blog/home.html")


def about(request):
    """
    About page
    :param request:
    :return:    """
    return render(request, "blog/about.html")