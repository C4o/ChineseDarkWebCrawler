"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import view
from DrakWeb.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^index/$', view.index),
    #the route of executing crawling
    # url(r'^Basic_crawler/$', Basic_crawler),
    # url(r'^Teach_crawler/$', Teach_crawler),
    # url(r'^Other_crawler/$', Other_crawler),
    # url(r'^Service_crawler/$', Service_crawler),
    # url(r'^Sex_crawler/$', Sex_crawler),
    # url(r'^Virtual_Source_crawler/$', Virtual_Source_crawler),
    # url(r'^Material_crawler/$', Material_crawler),
    # url(r'^Data_crawler/$', Data_crawler),
    # url(r'^Private_crawler/$', Private_crawler),
    # url(r'^CVV_crawler/$', CVV_crawler),
    #the route of checking database
    url(r'^Basic/$', view.Read_Basic),
    url(r'^Data/$', view.Read_Data),
    url(r'^Other/$', view.Read_Other),
    url(r'^Sex/$', view.Read_Sex),
    url(r'^Virtual_Source/$', view.Read_Virtual_Source),
    url(r'^Material/$', view.Read_Material),
    url(r'^Service/$', view.Read_Service),
    url(r'^Private/$', view.Read_Private),
    url(r'^CVV/$', view.Read_CVV),
    url(r'^Teach/$', view.Read_Teach),
    #the root of user login and logout
    url(r'^login/$', view.login),
    url(r'^regist/$', view.regist),
    url(r'^logout/$', view.logout)
]
