from django.urls import path

from .views import *

"""
The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


urlpatterns = [
    path('', home_view, name='home'),

    # user login, logout and registration url
    path('accounts/login', login_view, name='login'),  # login
    path('accounts/logout', logout_view, name='logout'),  # logout
    path('accounts/doctor-registration', doctor_signup_view, name='doctor-register'),  # doctor registration
    path('accounts/patient-registration', patient_signup_view, name='patient-register'),  # patient registration

    # doctor and patient feed url
    path('doctor-dashboard', doctor_dashboard, name='doctor-dashboard'),  # doctor dashboard
    path('patient-dashboard', patient_dashboard, name='patient-dashboard'),  # patient dashboard

    # doctor profile and patient profile
    path('doctor-profile/<str:pk>', doctor_profile_view, name='doctor-profile'),  # doctor profile
    path('patient-profile/<str:pk>', patient_profile_view, name='patient-profile'),  # patient profile

    # doctor and patient profile edit url
    path('update-doctor-profile', doctor_edit_profile, name='doctor-edit-profile'),  # doctor profile edit
    path('update-patient-profile',
         patient_edit_profile, name='patient-edit-profile'),  # patient profile edit

    # utilities
    path('accounts/account-settings', account_settings_view, name='account-settings'),  # account settings
    path('contact', contact_view, name='contact'),  # contact page
]
