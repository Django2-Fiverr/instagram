from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel

User = get_user_model()


class Relation(BaseModel):
    from_user = models.ForeignKey(User, related_name='followings',
                                  on_delete=models.CASCADE)

    to_user = models.ForeignKey(User, related_name='followers',
                                on_delete=models.CASCADE)

    confirmation = models.BooleanField(_('Confirmation'), default=False)

    def __str__(self):
        return str(self.confirmation)

    class Meta:
        verbose_name: _('Relation')
        verbose_name_plural: _('Relations')
        db_table = 'Relation'
