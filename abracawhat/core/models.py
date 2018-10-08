from model_utils import FieldTracker
from model_utils.models import TimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel

from abracawhat.core.utils import ChoicesUtil


class ModelUtilsMixin(TimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel):
    STATUS = ChoicesUtil.DEFAULT_STATUS

    tracker = FieldTracker()

    class Meta:
        abstract = True
