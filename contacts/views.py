#
# REPLACE the entire contents of this file
#
from django.shortcuts import render

# We are removing all Django-based login logic.
# The JavaScript in the templates will handle security
# by checking for the access token in localStorage.

def register_view(request):
    """Serves the blank register page."""
    # Point to your new folder: 'registration/register.html'
    return render(request, 'registration/register.html') 

def login_view(request):
    """Serves the blank login page."""
    # Point to your new folder: 'registration/login.html'
    return render(request, 'registration/login.html')

def logout_view(request):
    """Serves the logout action and redirects to the login page."""
    # Point to your new folder: 'registration/login.html'
    return render(request, 'registration/login.html')

def contact_list(request):
    """Serves the blank contact list page."""
    # This file is in the root, so no prefix is needed.
    return render(request, 'contact_list.html')

def contact_create(request):
    """Serves the blank form page for creating a new contact."""
    # This file is in the root, so no prefix is needed.
    return render(request, 'contact_form.html')

def contact_update(request, pk):
    """Serves the form page and passes the contact's PK to the template."""
    # This file is in the root, so no prefix is needed.
    return render(request, 'contact_form.html', {'contact_pk': pk})

def contact_delete(request, pk):
    """Serves the delete confirmation page and passes the PK."""
    # This file is in the root, so no prefix is needed.
    return render(request, 'contact_confirm_delete.html', {'contact_pk': pk})