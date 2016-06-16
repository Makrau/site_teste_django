from django.db import models
from django.utils import timezone

# Create your models here.


class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 200)
    news_text = models.TextField(null = False, default = "Preencha aqui sua notícia!", );
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    news_type = models.CharField(max_length = 50, default = 'Gerais')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#class User(models.Model):
