"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
#www.example.com-->example.com/app
urlpatterns = [
    path('catalog/',include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url='catalog')),
    path('accounts/',include('django.contrib.auth.urls'))
]
# the url below does the following
# 'accounts/',include('django.contrib.auth.urls')
# NOTE:SUPPOSED TO CREATE TEMPLATES FOR THESE
#AND IT HAS TO BE MADE AT THE PROJECT LEVEL CALLED REGISTRATION
# accounts/login/[name='login']
# accounts/logout/[name='logout']
# accounts/password_change/[name='password_change']
# accounts/password_change/done/[name='password_change_done']
# accounts/password_reset/[name='password_reset']
# accounts/password_reset/done/[name='password_reset_done']
# accounts/reset/<uidb64>/<token>/[name='password_reset_confirm']
# accounts/reset/done/[name='password_reset_complete']
