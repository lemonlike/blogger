# -*- coding: utf-8 -*-
__author__ = 'lemon'
__date__ = '2017/6/24 21:02'

import xadmin

from .models import MyArticle, Category


class MyArticleAdmin(object):
    list_display = ['title', 'category', 'add_time']
    search_fields = ['title', 'category']
    list_filter = ['title', 'category__cate_name', 'add_time']
    style_fields = {"content": "ueditor"}


class CategoryAdmin(object):
    list_display = ['cate_name', 'add_time']
    search_fields = ['cate_name']
    list_filter = ['cate_name', 'add_time']


xadmin.site.register(MyArticle, MyArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)