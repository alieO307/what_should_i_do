from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<category>/', views.category_options, name='category_options'),
    path('coin-toss/', views.coin_toss, name="coin_toss",),
    path('add_option/', views.add_option, name='add_option'),
]
 