from django.shortcuts import render

posts = [
    {
        'author': 'Al-Areef',
        'title': 'Blog post 2',
        'content': 'Blog post 1 content',
        'date_posted': 'November 4, 2023'
    },
    {
        'author': 'Al-Ameen',
        'title': 'Blog post 2',
        'content': 'Blog post 2 content',
        'date_posted': 'November 4, 2023'
    },
    {
        'author': 'Biggie',
        'title': 'Blog post 3',
        'content': 'Blog post 3 content',
        'date_posted': 'November 4, 2023'
    }
]


def home(request):
    """
    Home page
    :param request:
    :return:
    """
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)


def about(request):
    """
    About page
    :param request:
    :return:    """
    return render(request, "blog/about.html", {'title': 'About django'})
