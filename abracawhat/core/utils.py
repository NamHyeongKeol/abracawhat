from model_utils import Choices


class StringUtil:
    EMPTY = ''
    SPACE = ' '
    ZERO = '0'
    ONE = '1'
    TWO = '2'
    PROJECT_NAME = 'abracawhat'
    self = 'self'
    SELF = 'SELF'
    left = 'left'
    right = 'right'

    class Card:
        YONGYONG = 'YONGYONG'
        DARK = 'DARK'
        WIND = 'WIND'
        OWL = 'OWL'
        STORM = 'STORM'
        BLIZZARD = 'BLIZZARD'
        FIRE = 'FIRE'
        POTION = 'POTION'


class NumUtil:
    DEFAULT_HP = 6
    DEFAULT_SCORE = 0
    DEFAULT_ROUND = 1


class FieldUtil:
    MAX_NUMBER_OF_USERS_IN_GAME = 5


class ChoicesUtil:
    CARD_TYPES_BY_NAME = Choices(StringUtil.Card.YONGYONG,
                                 StringUtil.Card.DARK,
                                 StringUtil.Card.WIND,
                                 StringUtil.Card.OWL,
                                 StringUtil.Card.STORM,
                                 StringUtil.Card.BLIZZARD,
                                 StringUtil.Card.FIRE,
                                 StringUtil.Card.POTION,
                                 )

    CARD_TYPES_BY_NUM = Choices((1, StringUtil.Card.YONGYONG),
                                (2, StringUtil.Card.DARK),
                                (3, StringUtil.Card.WIND),
                                (4, StringUtil.Card.OWL),
                                (5, StringUtil.Card.STORM),
                                (6, StringUtil.Card.BLIZZARD),
                                (7, StringUtil.Card.FIRE),
                                (8, StringUtil.Card.POTION),
                                )

    DEFAULT_STATUS = Choices('DEFAULT')
    GAME_STATUS = Choices('CREATING', 'ONGOING', 'PENDING', 'DELETED', 'FINISHIED', )
    MOVE_STATUS = Choices('SUCCEED', 'FAILED', )
    CARD_STATUS = Choices('FIELD', 'SECRET', 'USED', 'SECRET_BUT_EXPOSED', 'STAND_BY', )


class ListUtil:
    CARD_LIST = ChoicesUtil.CARD_CHOICES
