# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Material(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class CVV(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Virtual_Source(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Basic(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Other(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Private(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Teach(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Sex(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class Service(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Topic_id = models.IntegerField(null=True)
    Topic_post_username = models.TextField(null=False)
    Topic_title = models.TextField(null=False)
    Topic_post_time = models.TextField(null=False)
    Deal_divide_sales = models.TextField(null=False)
    Topic_price_dollar = models.TextField(null=False)
    Topic_sales_status = models.TextField(null=False)
    Crwal_time = models.TextField(null=False)
    Catagory = models.TextField(null=False)

class User(models.Model):
    Username = models.TextField(primary_key=True, null=False)
    Password = models.TextField(null=False)
    ticket = models.TextField(null=True)