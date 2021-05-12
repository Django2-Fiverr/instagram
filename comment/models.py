from django.db import models
from user.models import User
from post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='كاربر')
    content = models.TextField(max_length=1000, null= True, verbose_name='متن پيام')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name='پست')
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='پاسخ')
    created = models.DateTimeFied(auto_now_add=True, verbose_name='تاريخ ايجاد')
    updated = models.DateTimeFied(auto_now= True, verbose_name='تاريخ')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='كاربر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='پيام')
    created = models.DateTimeFied(auto_now_add=True, verbose_name='تاريخ ايجاد')