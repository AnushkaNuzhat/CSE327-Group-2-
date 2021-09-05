from django.test import SimpleTestCase
from django.urls import reverse, resolve
from health_records.views import *


class TestUrls(SimpleTestCase):

    def test_health_record_home_view_url_is_resolved(self):
        url = reverse('health-record-home', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, health_record_home_view)

    def test_health_record_create_view_url_is_resolved(self):
        url = reverse('health-record-create')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, health_record_create_view)

    def test_health_record_detail_view_url_is_resolved(self):
        url = reverse('health-record-post-detail', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, health_record_detail_view)

    def test_health_record_update_view_url_is_resolved(self):
        url = reverse('health-record-post-update', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, health_record_update_view)

    def test_health_record_delete_view_url_is_resolved(self):
        url = reverse('health-record-post-delete', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, health_record_delete_view)
