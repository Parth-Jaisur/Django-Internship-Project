from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="homefile"),
    path('sports/',views.sportsnews,name="sportsnewsfile"),
    path('tranding/',views.trandingnews,name="trandingnewsfile"),
    path('top/',views.topnews,name="topnewsfile"),
    path('entertainment/', views.entertainmentnews, name="entertainmentnewsfile"),
    path('science/', views.sciencenews, name="sciencenewsfile"),
]