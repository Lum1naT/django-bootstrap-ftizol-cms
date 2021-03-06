
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
    path('event-signup', views.event_signup, name="event_signup"),
    path('my-account/', views.my_account, name="my_account"),
    path('frogot-password/', views.frogot_password, name="frogot_password"),

    path('events/ready-for/', views.upcoming_events,
         name="upcoming_events"),

    path('events/upcoming/', views.upcoming_events,
         name="upcoming_events"),

    path('events/upcoming/<int:event_id>', views.upcoming_event_detail,
         name="upcoming_event_detail"),


    path('test/find-all-workers/>', views.find_all_workers,
         name="find_all_workers"),

    path('test/find-worker/<int:worker_id>', views.find_worker,
         name="find_worker"),

]
