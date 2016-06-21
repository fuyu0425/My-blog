from django.shortcuts import render
from django.http import *
from .models import *
from datetime import datetime
from django.views.generic import DetailView,ListView

def article_list(request):
    article_list=Article.objects.all().filter(status='p')
    return render(request,'article_list.html',locals())
def article_draft_list(request):
    article_list=Article.objects.all().filter(status='d')
    return render(request,'draft_list.html',locals())
class ArticleDetailView(DetailView):
    model=Article
    template_name='detail.html'
    context_object_name="article"
    pk_url_kwarg = 'article_id'
