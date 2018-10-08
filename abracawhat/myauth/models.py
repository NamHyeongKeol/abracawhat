from django.contrib.auth.models import AbstractUser
from model_utils import FieldTracker, Choices
from model_utils.models import TimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel


class User(AbstractUser, TimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel):
    STATUS = Choices('PENDING', 'BASIC')

    tracker = FieldTracker()
