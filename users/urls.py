from django.urls import path
from users import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.create_or_update_user, name='user_create'),
    path('<int:id>/edit/', views.create_or_update_user, name='user_edit'),
    path('<int:id>/delete/', views.delete_user, name='user_delete'),
]
