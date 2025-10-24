#
# REPLACE the entire contents of this file
#
from django.contrib import admin
from django.urls import path, include
from contacts import views as contacts_views # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This is the main entry point. 
    # It sends all traffic to your 'contacts' app.
    path('', include('contacts.urls')),
    
    # Handle the root URL. Redirects to the login page.
    path('', contacts_views.login_view, name='root'),
]