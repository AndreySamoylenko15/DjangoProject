from django.contrib import admin
from django.urls import path, include
from quotes.views import author_quotes 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quotes.urls")),
    path("users/",include("users.urls")),
    path('author/<str:author_name>/quotes/', author_quotes, name='author_quotes'),
]
