from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class GenderChoice(IntegerChoices):
    MALE = (1, _('Male'))
    FEMALE = (0, _('Female'))
