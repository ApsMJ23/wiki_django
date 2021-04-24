from django.urls import path
from . import views

urlpatterns = [
    path('add_entry', views.add_entry, name='add_entry'),
    path('search_entry',views.search_entry, name = 'search_entry'),
    path('',views.index, name = 'index'),
    path("<str:title>",views.show_entry, name = 'show_entry'),

]