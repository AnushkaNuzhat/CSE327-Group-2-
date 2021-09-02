from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blood_donation.views import *


class TestUrls(SimpleTestCase):

    def test_post_blood_request_view_url_is_resolved(self):
        url = reverse('blood-donation-post-request')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, post_blood_request_view)

    def test_blood_donation_home_view_url_is_resolved(self):
        url = reverse('blood-donation-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, blood_donation_home_view)

    def test_blood_request_detail_view_url_is_resolved(self):
        url = reverse('blood-donation-request-detail', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, blood_request_detail_view)

    def test_update_blood_request_view_url_is_resolved(self):
        url = reverse('blood-donation-update-request', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, update_blood_request_view)

    def test_delete_blood_request_view_url_is_resolved(self):
        url = reverse('blood-donation-delete-request', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, delete_blood_request_view)
