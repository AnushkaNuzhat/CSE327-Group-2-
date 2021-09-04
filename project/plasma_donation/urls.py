from django.urls import path

from .views import *

urlpatterns = [
    path('', plasma_donation_home_view, name='plasma-donation-home'),
    path('post-request', post_plasma_request_view, name='plasma-donation-post-request'),
    path('update-request/<int:pk>', update_plasma_request_view, name='plasma-donation-update-request'),
    path('delete-request/<int:pk>', delete_plasma_request_view, name='plasma-donation-delete-request'),
    path('request-detail/<int:pk>', plasma_request_detail_view, name='plasma-donation-request-detail'),
    path('requests/<int:pk>', users_requests_view, name='users-plasma-requests'),
]
