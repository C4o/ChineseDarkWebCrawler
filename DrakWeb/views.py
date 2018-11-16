# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from .Crawler import darkweb

from django.shortcuts import render

# Create your views here.

def Basic_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(60, 'basic')
    cursor.close()
    return HttpResponseRedirect('/Basic/')

def Data_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(78, 'data')
    cursor.close()
    return HttpResponseRedirect('/Data/')

def Teach_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(84, 'teach')
    cursor.close()
    return HttpResponseRedirect('/Teach/')

def Other_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(37, 'other')
    cursor.close()
    return HttpResponseRedirect('/Other/')

def Service_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(57, 'service')
    cursor.close()
    return HttpResponseRedirect('/Service/')

def Private_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(80, 'private')
    cursor.close()
    return HttpResponseRedirect('/Private/')

def Virtual_Source_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(58, 'virtual_source')
    cursor.close()
    return HttpResponseRedirect('/Virtual_Source/')

def CVV_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(59, 'cvv')
    cursor.close()
    return HttpResponseRedirect('/CVV/')

def Material_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(82, 'material')
    cursor.close()
    return HttpResponseRedirect('/Material/')

def Sex_crawler(request):
    cursor = connection.cursor()
    darkweb.DarkCrawler(100, 'sex')
    cursor.close()
    return HttpResponseRedirect('/Sex/')