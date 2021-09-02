from user_control.models import UserModel
from django.db import models


class ArticleCategoryModel(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class ArticleModel(models.Model):
    """
    The Article model is used to store articles.

    Attributes:
        article_author: The author of the article.
        article_title: The title of the article.
        article_subtitle: The subtitle of the article.
        article_category: The category of the article.
        article_content: The content of the article.
        article_image: The image of the article.
        article_date_posted: The date the article was posted.
        article_slug: The slug of the article.
        article_totalViewCount: The number of views the article has.
    """
    article_author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=255)
    article_subtitle = models.CharField(max_length=255, null=True, blank=True)
    article_category = models.ForeignKey(ArticleCategoryModel, null=True, blank=True, on_delete=models.SET_NULL)
    article_content = models.TextField()
    article_image = models.ImageField(null=True, blank=True)
    article_date_posted = models.DateTimeField(auto_now_add=True)
    article_slug = models.SlugField(unique=True, null=True, blank=True)
    article_totalViewCount = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title + " by " + self.article_author.name
