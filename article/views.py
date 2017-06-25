# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View

from .models import MyArticle
# Create your views here.


class IndexView(View):
    """
    首页
    """
    def get(self, request):

        articles = MyArticle.objects.all().order_by("-add_time")
        return render(request, "index.html", {
            "articles": articles
        })


class ArticleContentView(View):
    """
    文章详情
    """
    def get(self, request, article_id):

        article = MyArticle.objects.get(id = int(article_id))

        return render(request, "post.html", {
            "article": article
        })