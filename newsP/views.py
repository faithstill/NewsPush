from django.shortcuts import render
from newsP.models import news
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    news_list = news.objects.all()
    return render_to_response('index.html',{'news_list':news_list})