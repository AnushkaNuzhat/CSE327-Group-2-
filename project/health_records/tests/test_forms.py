from django.test import SimpleTestCase
from health_records.views import *


class TestForms(SimpleTestCase):

    def test_RecordForm_from_valid_data(self):
        form = RecordForm(data={
            'title': "test_title",
            'content': "test_content",
        })
        self.assertTrue(form.is_valid())

    def test_RecordForm_form_no_data(self):
        form = RecordForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
