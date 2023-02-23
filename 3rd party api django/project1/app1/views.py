from django.shortcuts import render
import requests
#API_KEY = '71bc2a338a114460bf1437596f442fac'


# Create your views here.

def home(request):
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-01-19&sortBy=publishedAt&apiKey=71bc2a338a114460bf1437596f442fac'
    res = requests.get(url)
    data = res.json()
    articles = data['articles']
    
    context = {'articles':articles}

    return render(request,'app1/home.html',context)

