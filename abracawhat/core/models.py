from model_utils import FieldTracker
from model_utils.models import TimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel


class ModelUtilsMixin(TimeFramedModel, TimeStampedModel, StatusModel, SoftDeletableModel):
    tracker = FieldTracker()
