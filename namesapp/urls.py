from django.urls import path
from .views import CatNameList



urlpatterns = [
    path('cats/', CatNameList.as_view()),
]