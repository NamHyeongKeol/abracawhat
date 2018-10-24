import random

from django.conf import settings
from django.db import models, transaction

from abracawhat.core.models import ModelUtilsMixin
from abracawhat.core.utils import ChoicesUtil, NumUtil, StringUtil


class Game(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    winner = models.ForeignKey('Player', on_delete=models.CASCADE, db_index=True, null=True, related_name='+')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Player', related_name='games')

    @property
    def last_round(self):
        return self.rounds.order_by('num').last()

    @property
    def last_round_num(self):
        last_round = self.last_round
        if last_round is None:
            return 0
        else:
            return last_round.num

    @classmethod
    def create_game(cls, user_id_list=None, status=None):
        if user_id_list is None or len(user_id_list) < 2 or len(user_id_list) > 5:
            return None

        if status is None:
            status = ChoicesUtil.GAME_STATUS.ONGOING

        game = cls.objects.create(status=status)

        return game

    @classmethod
    @transaction.atomic(savepoint=False)
    def set_game(cls, user_id_list=None):
        game = cls.create_game(user_id_list=user_id_list)

        game.set_players(user_id_list=user_id_list)

        game.set_round()

        return game

    @transaction.atomic(savepoint=False)
    def set_players(self, user_id_list=None):
        random.shuffle(user_id_list)
        left, first_player = None, None
        for user_id in user_id_list:
            player = Player.create_player(user_id=user_id, game_id=self.id, left=left)

            if user_id_list[0] == user_id:
                first_player = player
            else:
                left.right = player
                left.save()

            left = player

        left.right = first_player
        first_player.left = left

        return self

    def set_round(self):
        round = Round.create_round(game_id=self.id)

        return round


class Player(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True, related_name='players')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, db_index=True, related_name='players')
    left = models.ForeignKey(StringUtil.self, on_delete=models.CASCADE, null=True, related_name='+')
    right = models.ForeignKey(StringUtil.self, on_delete=models.CASCADE, null=True, related_name='+')

    @classmethod
    def create_player(cls, user_id=None, game_id=None, left=None, right=None, status=None):
        if user_id is None or game_id is None:
            return None

        if status is None:
            status = ChoicesUtil.GAME_STATUS.ONGOING

        player = cls.objects.create(user_id=user_id, game_id=game_id, left=left, right=right, status=status)

        return player


class Round(ModelUtilsMixin):
    STATUS = ChoicesUtil.GAME_STATUS
    game = models.ForeignKey(Game, on_delete=models.CASCADE, db_index=True, related_name='rounds')
    num = models.IntegerField(default=NumUtil.DEFAULT_ROUND, db_index=True)

    @classmethod
    @transaction.atomic(savepoint=False)
    def create_round(cls, game_id=None, status=None):
        if game_id is None:
            return None

        if status is None:
            status = ChoicesUtil.GAME_STATUS.ONGOING

        round = cls.objects.create(game_id=game_id, status=status, num=Game.objects.get(id=game_id).last_round_num + 1)

        return round


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
        return self.player.left.player_rounds.get(round=self.round)

    @property
    def right(self):
        return self.player.right.player_rounds.get(round=self.round)


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
