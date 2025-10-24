#
# REPLACE the entire contents of this file
#
from django.urls import path
from . import views

urlpatterns = [
    # Auth URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Contact CRUD URLs
    # 'contact_list' is the main page after login
    path('contacts/', views.contact_list, name='contact_list'),
    path('new/', views.contact_create, name='contact_create'),
    path('edit/<int:pk>/', views.contact_update, name='contact_update'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
    
    # Redirect root to login
    path('', views.login_view, name='root-redirect'),
]