from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class News(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 200)
    news_text = models.TextField(null = False, default = "Preencha aqui sua notícia!");
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    news_type = models.CharField(max_length = 50, default = 'Gerais')
    #notifications = BooleanField(default = False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey('news.News', related_name = 'comments')
    author = models.CharField(max_length = 150, default = "Anônimo")
    comment_text = models.TextField(null = False, default = "Escreva seu comentário aqui!")
    created_date = models.DateTimeField(default = timezone.now)

    def approve_comment(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text

class Notification(models.Model):
    news = models.ForeignKey('news.News', related_name = 'notifications')
    comment = models.ForeignKey('news.Comment', related_name = 'notifications')
    user = models.ForeignKey('auth.User', related_name = 'notifications')
    created_date = models.DateTimeField(default = timezone.now)

    def notify(self):
        #self.was_seen = True
        self.delete()

@receiver(post_save, sender = Comment)
def notify_comment(sender, instance, **kwargs):
    print ("sinal disparado!")
    comments  = Comment.objects.filter(comment_text=instance).order_by('-created_date')
    news = News.objects.filter(title=comments[0].news)

    notification = Notification()
    notification.news = news[0]
    notification.comment = comments[0]
    notification.user = news[0].author

    notification.save()
    print("salvou a notificação!\n")