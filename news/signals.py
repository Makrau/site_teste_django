 from django.db.models.signals import post_save, pre_save
 from django.dispatch import receiver
 from news.models import News, Comment, Notification

@receiver(post_save, sender = Comment, weak = False)
def notify_comment(sender, **kwargs):
    print "sinal disparado!"
    news = get_object_or_404(News, instance.news.pk)
    comment = get_object_or_404(Comment, instance.pk)

    notification = Notification()
    notification.news = news.pk
    notification.comment = comment.pk
    notification.user = news.author

    notification.save()


#post_save.connect(notify_comment, sender = Comment)
pre_save.connect(notify_comment, sender = Comment, weak = False)