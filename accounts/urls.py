from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('reset/', views.reset, name='accounts.reset'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path('resetpassword/', views.resetpassword, name='accounts.resetpassword'),
]