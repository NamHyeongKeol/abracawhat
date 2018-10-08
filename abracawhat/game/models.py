from django.conf import settings
from django.db import models

from abracawhat.core.models import ModelUtilsMixin
from abracawhat.core.utils import ChoicesUtil, NumUtil, StringUtil


class Game(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    winner = models.ForeignKey('Player', on_delete=models.CASCADE, db_index=True, related_name='+')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Player', related_name='games')


class Player(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True, related_name='players')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, db_index=True, related_name='players')
    left = models.ForeignKey(StringUtil.self, on_delete=models.CASCADE, related_name='+')
    right = models.ForeignKey(StringUtil.self, on_delete=models.CASCADE, related_name='+')


class Round(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    game = models.ForeignKey(Game, on_delete=models.CASCADE, db_index=True)
    num = models.IntegerField(default=NumUtil.DEFAULT_SCORE, db_index=True)


class PlayerRound(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    player = models.ForeignKey(Player, on_delete=models.CASCADE, db_index=True, related_name='player_rounds')
    round = models.ForeignKey(Round, on_delete=models.CASCADE, db_index=True, related_name='player_rounds')
    hp = models.IntegerField(default=NumUtil.DEFAULT_HP, db_index=True)
    score = models.IntegerField(default=NumUtil.DEFAULT_SCORE, db_index=True)

    @property
    def user(self):
        return self.player.user

    @property
    def game(self):
        return self.player.game

    @property
    def left(self):
        return self.player.left

    @property
    def right(self):
        return self.player.right


class Turn(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    player_round = models.ForeignKey(PlayerRound, on_delete=models.CASCADE, db_index=True, related_name='turns')


class Move(ModelUtilsMixin):
    STATUS = ChoicesUtil.MOVE_STATUS
    player_round = models.ForeignKey(PlayerRound, on_delete=models.CASCADE, db_index=True, related_name='moves')
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE, db_index=True, related_name='moves')


class Card(ModelUtilsMixin):
    STATUS = ChoicesUtil.CARD_STATUS
    player_round = models.ForeignKey(PlayerRound, on_delete=models.CASCADE, db_index=True, null=True,
                                     related_name='cards')
    round = models.ForeignKey(Round, on_delete=models.CASCADE, db_index=True, related_name='cards')
    move = models.ForeignKey(Move, on_delete=models.CASCADE, db_index=True, null=True, related_name='cards')
    name = models.CharField(max_length=100, choices=ChoicesUtil.CARD_CHOICES, db_index=True)
