from django.shortcuts import render,redirect
from .models import SearchHistory
import requests
# Create your views here.
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
def index(request):
    weather_data=None
    history=SearchHistory.objects.order_by('-searched_at')[:5]
    if request.method=="POST":
        city=request.POST.get('name')
        url=f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        res=requests.get(url)
        data=res.json()
        if res.status_code==200:
            weather_data = {
                "temp":data["current"]["temp_c"],
                "humidity":data["current"]["humidity"],
                "description": data["current"]["condition"]["text"],
                "city":data["location"]["name"],
            }
            SearchHistory.objects.create(temp=weather_data["temp"],humidity=weather_data["humidity"], city=weather_data["city"],description=weather_data["description"])
    return render(request,'index.html',{"history":history})
def clear(request,id):
    SearchHistory.objects.get(id=id).delete()
    history=SearchHistory.objects.order_by('-searched_at')[:5]
    return redirect('index')
def clearall(request):
    SearchHistory.objects.all().delete()
    history=SearchHistory.objects.order_by('-searched_at')[:5]
    return redirect(index)
