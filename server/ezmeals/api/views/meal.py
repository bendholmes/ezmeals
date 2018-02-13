from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from ezmeals.models import Meal
from ezmeals.api.serializers import MealSerializer


class MealViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
