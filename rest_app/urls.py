from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_app import views

urlpatterns = [
    path('rest_app/', views.SnippetList.as_view()),
    path('rest_app/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)