from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices

from abracawhat.core.models import ModelUtilsMixin
from abracawhat.game.models import Game


class User(AbstractUser, ModelUtilsMixin):
    STATUS = Choices('PENDING', 'BASIC')

    games = models.ManyToManyField(Game, through='Player', related_name='users')
