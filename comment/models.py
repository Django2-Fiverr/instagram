from django.db import models
from django.contrib.auth import get_user_model
# from post.models import Post

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='كاربر')
    content = models.TextField(max_length=1000, null=True,help_text='پيام خود را بنويسيد...', verbose_name='متن پيام')
    # post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comment', null=True, verbose_name='پست')
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE,related_name='reply', null=True, blank=True, verbose_name='پاسخ')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ ايجاد')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='تاريخ')

    class Meta:
        ordering = ['-created']
        verbose_name = ('كامنت')
        verbose_name_plural = ('كامنت ها')

    def __str__(self):
        return f'{self.user}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='كاربر')
    # post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_like', null=True, verbose_name='پست')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='comment_like', null=True, verbose_name='پيام')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ ايجاد')

    class Meta:
        verbose_name = ('لايك')
        verbose_name_plural = ('لايك ها')

    def __str__(self):
        return f'{self.user}'


class TaggedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='كاربر')
    # post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_tag', null=True, verbose_name='پست')

    class Meta:
        verbose_name = ('تگ')
        verbose_name_plural = ('تگ ها')

    def __str__(self):
        return f'{self.user}'