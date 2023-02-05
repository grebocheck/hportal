from django.db import models
from tinymce.models import HTMLField

# For user relationship with reviews
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Назва")
    cover_image = models.ImageField(upload_to="article/images/", verbose_name="Превью")
    body = HTMLField(verbose_name="Стаття")

    modifiedAt = models.DateTimeField(auto_now=True, null=True, verbose_name="Створено")
    createdAt = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Змінено")

    featured = models.BooleanField(default=False, verbose_name="в Рекомендовані?")

    file_1 = models.FileField(null=True, upload_to="article/files/", verbose_name="Прикріплений файл 1", blank=True)
    file_2 = models.FileField(null=True, upload_to="article/files/", verbose_name="Прикріплений файл 2", blank=True)
    file_3 = models.FileField(null=True, upload_to="article/files/", verbose_name="Прикріплений файл 3", blank=True)

    # Relationship -> One to Many
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=30, verbose_name="Назва")
    body = models.TextField(verbose_name="Детальний коментар")
    createdAt = models.DateTimeField(auto_now=True)

    # Relationship -> one to many
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    # Relationship -> one to many
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        username = self.user.username
        return username.upper() + " ------ " + self.article.title
