from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('web-projects', views.web_project, name='web-development'),

]