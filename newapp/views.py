from django.shortcuts import render
import requests
# Create your views here.
record = {}
def home(request):
    url = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    mydata3 = url.json()
    record['allnews'] = mydata3
    context = {
        'card_data_list': record,
    }

    return render(request, 'home.html', context)


def sportsnews(request):
    record={}
    url3 = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    mydata3 = url3.json()
    record['sportsdata']=mydata3

    context = {
        'card_data_list': record,
    }

    return render(request, 'sportsnews.html', context)


def trandingnews(request):
    url = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
    mydata3 = url.json()
    record['tredingnews'] = mydata3
    context = {
        'card_data_list': record,
    }

    return render(request, 'trandingnews.html', context)

def topnews(request):
    url = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
    mydata3 = url.json()
    record['topnews'] = mydata3
    context = {
        'card_data_list': record,
    }

    return render(request, 'topnews.html', context)


def entertainmentnews(request):
    url = requests.get("https://inshorts.me/news/topics/entertainment")
    mydata3 = url.json()
    record['entertainmentnews'] = mydata3
    context = {
        'card_data_list': record,
    }

    return render(request, 'entertainmentnews.html', context)


def sciencenews(request):
    url = requests.get("https://inshorts.me/news/topics/science")
    mydata3 = url.json()
    record['sciencenews'] = mydata3
    context = {
        'card_data_list': record,
    }

    return render(request, 'sciencenews.html', context)
