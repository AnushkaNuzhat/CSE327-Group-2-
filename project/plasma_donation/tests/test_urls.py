from django.test import SimpleTestCase
from django.urls import reverse, resolve

from plasma_donation.views import *


class TestUrls(SimpleTestCase):

    def test_plasma_donation_home_view_url_is_resolved(self):
        url = reverse('plasma-donation-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, plasma_donation_home_view)

    def test_post_plasma_request_view_url_is_resolved(self):
        url = reverse('plasma-donation-post-request')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, post_plasma_request_view)

    def test_update_plasma_request_view_url_is_resolved(self):
        url = reverse('plasma-donation-update-request', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, update_plasma_request_view)

    def test_delete_plasma_request_view_url_is_resolved(self):
        url = reverse('plasma-donation-delete-request', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, delete_plasma_request_view)

    def test_plasma_request_detail_view_url_is_resolved(self):
        url = reverse('plasma-donation-request-detail', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, plasma_request_detail_view)

    def test_users_requests_view_url_is_resolved(self):
        url = reverse('users-plasma-requests', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, users_requests_view)
