# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Category(models.Model):
    cate_name = models.CharField(verbose_name=u"类别", max_length=20)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"文章类别"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.cate_name


class MyArticle(models.Model):
    title = models.CharField(verbose_name=u"标题", max_length=50)
    category = models.ForeignKey(Category, verbose_name=u"文章类别")
    content = UEditorField(verbose_name=u"文章内容", width=700, height=600, imagePath="article/ueditor/",
                          filePath="article/ueditor/", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


