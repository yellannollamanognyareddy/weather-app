
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('clear/<int:id>/',views.clear,name='clear'),
    path('clearall/',views.clearall,name='clearall')
]
