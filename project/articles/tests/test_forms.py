from django.test import SimpleTestCase
from articles.views import *
from articles.forms import *


class TestForms(SimpleTestCase):

    def test_ArticleForm_from_valid_data(self):
        form = ArticleForm(data={
            'article_title': "test title",
            'article_content': "test content",
        })
        self.assertTrue(form.is_valid())

    def test_ArticleForm_form_no_data(self):
        form = ArticleForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
