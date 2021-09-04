from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_control.urls')),
    path('appointments/', include('appointments.urls')),
    path('articles/', include('articles.urls')),
    path('blood-donation/', include('blood_donation.urls')),
    path('plasma-donation/', include('plasma_donation.urls')),
    path('patient-community/', include('patient_community.urls')),
    path('health-advisor/', include('health_advisor.urls')),
    path('health-records/', include('health_records.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
