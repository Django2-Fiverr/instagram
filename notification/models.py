from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel

User = get_user_model()


class Notification(BaseModel):
    user = models.ForeignKey(User,
                             related_name='notifications',
                             on_delete=models.CASCADE)


class MessageNotification(BaseModel):
    user = models.ForeignKey(User,
                             related_name='message_notifications',
                             on_delete=models.CASCADE)
    check = models.BooleanField(_('check'), default=False)

    notification = models.ForeignKey(Notification,
                                     related_name='messages',
                                     on_delete=models.CASCADE)
    # TODO I Must deploy This relation as The Message model is ready
    # message = models.OneToOneField(Message,
    #                                on_delete=models.CASCADE)


class CommentNotification(BaseModel):
    user = models.ForeignKey(User,
                             related_name='comment_notifications',
                             on_delete=models.CASCADE)

    notification = models.ForeignKey(Notification,
                                     related_name='comments',
                                     on_delete=models.CASCADE)
    check = models.BooleanField(_('check'), default=False)

    # TODO I Must deploy This relation as The Comment model is ready
    # comment = models.OneToOneField(Comment, related_name='notifications',
    #                             on_delete=models.CASCADE)


class LikeNotification(BaseModel):
    user = models.ForeignKey(User,
                             related_name='like_notifications',
                             on_delete=models.CASCADE)

    notification = models.ForeignKey(Notification,
                                     related_name='likes',
                                     on_delete=models.CASCADE)
    check = models.BooleanField(_('check'), default=False)

    # TODO I Must deploy This relation as The like model is ready
    # like = models.OneToOneField(Like, related_name='notifications',
    #                          on_delete=models.CASCADE)


class FollowRequestNotification(BaseModel):
    user = models.ForeignKey(User,
                             related_name='follow_requests',
                             on_delete=models.CASCADE)

    notification = models.ForeignKey(Notification,
                                     related_name='follow_requests',
                                     on_delete=models.CASCADE)

    check = models.BooleanField(_('check'), default=False)

    # TODO I must complete this section
