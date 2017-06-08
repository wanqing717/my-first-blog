# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Post#导入Post模型
from django.utils import timezone


#views是连接数据库中的模型和模板的
def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


