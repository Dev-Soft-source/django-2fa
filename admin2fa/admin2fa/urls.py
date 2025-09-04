"""
URL configuration for admin2fa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django_otp.decorators import otp_required
from django.urls import path, include

urlpatterns = [
    # Protect admin with OTP
    path('admin/', otp_required(admin.site.urls)),

    # Include two_factor URLs with namespace correctly
    path('', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),

    # Optional local app
    path('', include('accounts.urls')),
]
