from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_bleach.models import BleachField

User = get_user_model()
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=255,
    )
    body = BleachField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        # get_user_model(),
        User,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse("article_detail", kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.comment
        
    def get_absolute_url(self):
        kwargs = {
            'pk': self.article.id,
            'slug': self.article.slug
        }
        return reverse("article_detail", kwargs=kwargs)
        #return reverse("article_detail", args=[str(self.article.id)])
        
    