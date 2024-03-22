from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_page, name='projects_page'),
    # path('', views.home, name='home'),
]