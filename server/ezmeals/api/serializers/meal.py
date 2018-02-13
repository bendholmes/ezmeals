from rest_framework.serializers import ModelSerializer

from ezmeals.models import Meal


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ('name', 'image',)
