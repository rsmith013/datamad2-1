from django.urls import path, include
from django.contrib.auth import views as auth_views
from datamad2 import views

urlpatterns = [
    path('', views.grant_list, name='grant_list'),
    path('routing_classification', views.routing_classification, name='routing_classification'),
    path('grant/<int:pk>/', views.grant_detail, name='grant_detail'),
    path('grant/<int:pk>/claim', views.claim, name='claim'),
    path('accounts/', include('django.contrib.auth.urls',)),
    path('accounts/', views.my_account, name='my_account'),
    path('grant/<int:pk>/change_claim/', views.change_claim, name='change_claim'),
    path('grant/<int:pk>/unclaim', views.unclaim, name='unclaim'),
    path('grant/<int:pk>/history', views.grant_history, name='grant_history'),
]
