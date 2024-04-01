from django.urls import path,include

from . import views

app_name = "quotes"


urlpatterns = [
    path("", views.main, name='main'),
    path("<int:page>", views.main, name='root_paginate'),
    path("add_author", views.add_author, name="add_author"),
    path("add_quote", views.add_quote, name="add_quote"),
    path('tag/', views.tag, name='tag'),
]
