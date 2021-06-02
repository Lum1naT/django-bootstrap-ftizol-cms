
"""example URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('my-account/', views.my_account, name="my_account"),
    path('frogot-password/', views.frogot_password, name="frogot_password"),
    path('upcoming-events/', views.upcoming_events, name="upcoming_events"),
]
