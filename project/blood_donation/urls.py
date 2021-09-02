from django.urls import path

from .views import *

urlpatterns = [
    path('', blood_donation_home_view, name='blood-donation-home'), # path for home page
    path('post-request', post_blood_request_view, name='blood-donation-post-request'), # path for post request
    path('update-request/<int:pk>', update_blood_request_view, name='blood-donation-update-request'), # path for update request
    path('delete-request/<int:pk>', delete_blood_request_view, name='blood-donation-delete-request'), # path for delete request
    path('request-detail/<int:pk>', blood_request_detail_view, name='blood-donation-request-detail'), # path for request detail
    path('requests/<int:pk>', users_requests_view, name='users-requests'), # path for user requests
]
