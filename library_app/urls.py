# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_books, name='display_books'),
    # path('add_book/', views.add_book, name='add_book'),
    # path('add_category/', views.add_category, name='add_category'),
    # path('block_concurrent/<int:concurrent_id>/', views.block_concurrent, name='block_concurrent'),
    path('search_books/', views.search_books, name='search_books'),
    path('register/', views.register_concurrent, name='register_concurrent'),
    path('login/', views.login_concurrent, name='login_concurrent'),
]
