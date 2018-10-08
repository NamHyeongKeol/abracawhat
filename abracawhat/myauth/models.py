from django.contrib.auth.models import AbstractUser
from model_utils import FieldTracker, Choices

from abracawhat.core.models import ModelUtilsMixin


class User(AbstractUser, ModelUtilsMixin):
    STATUS = Choices('PENDING', 'BASIC')
