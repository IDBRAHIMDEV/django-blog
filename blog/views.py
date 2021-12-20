from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):

    articles = Article.objects.all()
    return render(request, "blog/index.html", {"articles": articles})


def create(request):

    form = ArticleForm()
    return render(request, "blog/create.html", {"form": form})


def edit(request, id):
    return render(request, "blog/edit.html")


def show(request, id):

    article = Article.objects.get(pk=id)
    return render(request, "blog/show.html", {"article": article})
